# Manual Funcional: Docs Agent

## 1. Funcionalidad y Objetivo
El **Docs Agent** (Agente de Documentación) se encarga de estructurar, formatear y generar documentos de texto complejos (como manuales, reportes ejecutivos, contratos o minutas). Soporta la generación de archivos de Microsoft Word (`.docx`) y archivos portables de documento (`.pdf`) utilizando herramientas de formateo de alta calidad como `WeasyPrint` y `python-docx`.
Adicionalmente, este agente cuenta con el permiso exclusivo dentro de OpenSwarm para realizar la subida automatizada de archivos a carpetas compartidas de Google Drive (`UploadToDrive`).

*   **Objetivo:** Proporcionar un redactor técnico de nivel senior que tome notas sueltas, esquemas o transcripciones de video y los convierta en documentos listos para su publicación o entrega formal.

---

## 2. Acceso y Permisos según el Rol

| Permiso / Capacidad | Administrador (César Lenin) | Desarrollador (Antigravity/Hermes) | Usuario Final / Invitado |
| :--- | :---: | :---: | :---: |
| **Subir archivos a carpetas de Google Drive**| Sí (Control total) | Sí (Automático) | No |
| **Generar Documentos Word / PDF** | Sí | Sí | Sí |
| **Definir Estilos de Reportes (CSS)** | Sí | Sí | No |
| **Acceso a Carpeta Compartida de Drive** | Sí | Sí | Sí (Lectura limitada) |
| **Editar Documentos Existentes** | Sí | Sí | No (Solo vía prompt) |

### 2.1 Rol: Administrador
*   **Qué puede ver:** Todos los documentos generados e indexados, así como las rutas locales y carpetas de destino de Google Drive.
*   **Acciones permitidas:** Solicitar manuales técnicos oficiales, actualizar documentación de Zentia o Dynoflow y cargar sus entregables directamente a la carpeta de su tesis.

### 2.2 Rol: Desarrollador
*   **Qué puede ver:** Las trazas de compilación de `WeasyPrint` (errores de renderizado CSS/HTML) y la configuración de tokens de acceso para la carga en Google Drive.
*   **Acciones permitidas:** Modificar la lógica de plantillas HTML y ajustar la herramienta de subida en `/docs_agent/tools/UploadToDrive.py`.

### 2.3 Rol: Usuario Final
*   **Qué puede ver:** Un archivo PDF formateado e impecable para descargar.
*   **Acciones permitidas:** Pedir resúmenes de textos, reformatear minutas o corregir la redacción y ortografía de un texto.
