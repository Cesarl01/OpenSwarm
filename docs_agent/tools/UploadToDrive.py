from agency_swarm.tools import BaseTool
from pydantic import Field
import os
import json
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

class UploadToDrive(BaseTool):
    """
    Sube un archivo local directamente a Google Drive utilizando las credenciales de Hermes.
    """
    local_file_path: str = Field(
        ..., description="La ruta local completa del archivo a subir, por ejemplo /var/www/resumen_ai_news.md"
    )
    folder_id: str = Field(
        None, description="ID opcional de la carpeta destino en Google Drive. Si no se especifica, se subirá a la raíz."
    )
    
    def run(self):
        token_path = os.path.expanduser("~/.hermes/google_token.json")
        if not os.path.exists(token_path):
            return "Error: No se encontró el token de Google. Verifica la autenticación."
            
        with open(token_path, "r") as f:
            creds_data = json.load(f)
            
        creds = Credentials.from_authorized_user_info(creds_data)
        service = build('drive', 'v3', credentials=creds)
        
        file_name = os.path.basename(self.local_file_path)
        file_metadata = {'name': file_name}
        
        if self.folder_id:
            file_metadata['parents'] = [self.folder_id]
            
        try:
            import mimetypes
            mime_type, _ = mimetypes.guess_type(self.local_file_path)
            if not mime_type:
                mime_type = 'application/octet-stream'
                
            media = MediaFileUpload(self.local_file_path, mimetype=mime_type, resumable=True)
            file = service.files().create(body=file_metadata, media_body=media, fields='id').execute()
            
            return f"Éxito: Archivo '{file_name}' subido correctamente a Google Drive con el ID: {file.get('id')}"
        except Exception as e:
            return f"Error al subir archivo a Google Drive: {str(e)}"
