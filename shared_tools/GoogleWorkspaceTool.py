from pydantic import Field
from agency_swarm.tools import BaseTool
import json
import os
from pathlib import Path
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseUpload, MediaIoBaseDownload
import io

class GoogleWorkspaceTool(BaseTool):
    """
    Interact with Google Workspace (Google Drive, Docs, Sheets).
    Allows listing files, reading contents, and writing/uploading new files.
    """
    
    action: str = Field(
        ..., description="The action to perform: 'list', 'read', 'write', or 'search'."
    )
    query: str = Field(
        default="", description="Search query for 'list' or 'search' actions. For example: name contains 'report'"
    )
    file_id: str = Field(
        default="", description="The Google Drive file ID to read or update."
    )
    filename: str = Field(
        default="", description="The name of the file to create or read."
    )
    content: str = Field(
        default="", description="The content to write to the file."
    )
    mime_type: str = Field(
        default="text/plain", description="The mime type of the file to create (e.g., text/plain, text/csv, application/vnd.google-apps.document)."
    )

    def run(self):
        token_path = Path(os.path.expanduser("~/.hermes/google_token.json"))
        if not token_path.exists():
            return "Error: Authentication token not found. Please authenticate first."
        
        try:
            creds = Credentials.from_authorized_user_file(str(token_path))
            drive_service = build('drive', 'v3', credentials=creds)
        except Exception as e:
            return f"Error authenticating with Google Drive: {str(e)}"
        
        try:
            if self.action in ['list', 'search']:
                results = drive_service.files().list(
                    q=self.query if self.query else None,
                    pageSize=20, fields="nextPageToken, files(id, name, mimeType)"
                ).execute()
                items = results.get('files', [])
                if not items:
                    return "No files found."
                return json.dumps(items, indent=2)
                
            elif self.action == 'read':
                if not self.file_id:
                    return "Error: file_id is required for read action."
                
                # Check mime type to see if we need to export (Docs, Sheets) or get (raw files)
                file_meta = drive_service.files().get(fileId=self.file_id, fields="name, mimeType").execute()
                mime = file_meta.get("mimeType", "")
                
                if "application/vnd.google-apps.document" in mime:
                    request = drive_service.files().export_media(fileId=self.file_id, mimeType='text/plain')
                elif "application/vnd.google-apps.spreadsheet" in mime:
                    request = drive_service.files().export_media(fileId=self.file_id, mimeType='text/csv')
                else:
                    request = drive_service.files().get_media(fileId=self.file_id)
                
                fh = io.BytesIO()
                downloader = MediaIoBaseDownload(fh, request)
                done = False
                while done is False:
                    status, done = downloader.next_chunk()
                
                return fh.getvalue().decode('utf-8')
                
            elif self.action == 'write':
                if not self.content:
                    return "Error: content is required for write action."
                
                fh = io.BytesIO(self.content.encode('utf-8'))
                media = MediaIoBaseUpload(fh, mimetype=self.mime_type, resumable=True)
                
                if self.file_id:
                    # Update existing file
                    updated_file = drive_service.files().update(
                        fileId=self.file_id,
                        media_body=media
                    ).execute()
                    return f"Successfully updated file {updated_file.get('name')} (ID: {updated_file.get('id')})"
                else:
                    if not self.filename:
                        return "Error: filename is required when creating a new file."
                    file_metadata = {'name': self.filename, 'mimeType': self.mime_type}
                    new_file = drive_service.files().create(
                        body=file_metadata,
                        media_body=media,
                        fields='id, name'
                    ).execute()
                    return f"Successfully created file {new_file.get('name')} (ID: {new_file.get('id')})"
            else:
                return f"Unsupported action: {self.action}"
                
        except Exception as e:
            return f"Error executing {self.action}: {str(e)}"
