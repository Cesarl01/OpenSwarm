# Memory.md - Registro Histórico de Aprendizajes y Correcciones

Este archivo registra los errores históricos del proyecto Hermes, la Arquitectura Cybite y el sistema OpenSwarm, junto con las soluciones implementadas. **Siempre se debe consultar este archivo antes de realizar cualquier acción para evitar la regresión de fallos.**

---

## 1. Límite de Crédito y Rate Limits en OpenRouter

### **Error Detectado**
Al interactuar con modelos comerciales en OpenRouter, se agotaba el saldo o crédito, provocando el fallo del sistema y bloqueando la comunicación de los agentes de Hermes y OpenSwarm.

### **Solución Aplicada**
*   Se configuró una **cadena de fallback robusta** en `config.yaml` (`fallback_providers`) que redirige las solicitudes de manera automática a modelos 100% gratuitos y de alto rendimiento cuando el proveedor primario falla.
*   Modelos gratuitos prioritarios asignados en la cadena:
    1.  `meta-llama/llama-3.3-70b-instruct:free` (principal de respaldo).
    2.  `google/gemma-4-31b-it:free`.
    3.  `qwen/qwen3-next-80b-a3b-instruct:free`.
    4.  `z-ai/glm-4.5-air:free`.
*   Se prioriza el uso nativo de Google Gemini (`gemini-2.0-flash`) utilizando el `GEMINI_API_KEY` directo para evitar intermediarios cuando sea posible.

---

## 2. Búsqueda y Manejo de Google Drive a través del Skill `google-workspace`

### **Error Detectado**
*   **Intento de uso de `gdrive_automation`:** Intentos erróneos de invocar automatizaciones inexistentes.
*   **HttpError 400 por sintaxis incorrecta:** El uso de filtros como `parents = '...'` o `parents in '...'` en la API de Google Drive provoca fallos HTTP.
*   **Uso de IDs largos:** Intentar que el usuario (que usualmente interactúa por voz o interfaz simplificada) provea o digite IDs de Drive.

### **Solución Aplicada**
*   **Comandos Directos:** Siempre ejecutar comandos a través del script oficial `google_api.py` mediante la terminal:
    `/home/administrador/Hermes-Agent/venv/bin/python /home/administrador/.hermes/skills/productivity/google-workspace/scripts/google_api.py`
*   **Sintaxis Correcta de Búsqueda:** Utilizar estrictamente `'ID_CARPETA' in parents and trashed = false` en las búsquedas en Drive.
*   **Flag Obligatorio:** Agregar siempre `--raw-query` al final de cualquier comando de búsqueda avanzada que involucre operadores lógicos (`and`, `or`, `in parents`).
*   **Interacción de Lenguaje Natural Autónoma:**
    *   *NUNCA* solicitar IDs al usuario.
    *   Efectuar búsquedas en segundo plano (`drive search`) usando palabras clave provistas por el usuario.
    *   Presentar listas numeradas amigables (ej: "1. Tesis de Maestría.mp4") y mapear de forma interna los números a los IDs correspondientes.
*   **Subida a Google Drive:** Delegar siempre la subida o movimiento de archivos al `Docs Agent` de OpenSwarm mediante el puente:
    `python /home/administrador/.hermes/openswarm_bridge.py "Sube el archivo X a Google Drive usando tu herramienta UploadToDrive" --agent "Docs Agent"`

---

## 3. Inicialización de la API de Gemini en `agency-swarm`

### **Error Detectado**
Al inicializar la arquitectura de multi-agentes de OpenSwarm mediante `agency-swarm`, se producían excepciones de `asyncio` y errores tipo `OpenAIError` por falta de credenciales o mal mapeo del backend de inferencia.

### **Solución Aplicada**
*   Se corrigió la inicialización del cliente Gemini dentro del framework de agentes asegurando que el token de `GEMINI_API_KEY` se propague de manera limpia a las clases de inicialización.
*   Se inyecta un mock/configuración compatible de OpenAI para satisfacer al core de `agency-swarm` cuando utiliza dependencias cruzadas de OpenAI, canalizando la inferencia real hacia el SDK de Gemini o a OpenRouter de forma estable.

---

## 4. Truncamiento de Respuestas en la Integración con Telegram

### **Error Detectado**
El bot de Telegram de Hermes fallaba o enviaba mensajes truncados cuando las respuestas generadas por los agentes especialistas o el puente superaban el límite máximo de caracteres de Telegram (4096 caracteres).

### **Solución Aplicada**
*   Se implementó un mecanismo de **chunking de mensajes** en el gateway de Telegram (`bin/tirith` y scripts asociados).
*   Las respuestas que superan los 4000 caracteres se fragmentan inteligentemente respetando saltos de línea, bloques de código markdown y listas, enviándose en múltiples mensajes encadenados.

---

## 5. Restauración y Backup de Bases de Datos (Zentia, DynoFlow y Hermes)

### **Error Detectado**
Operaciones de actualización del sistema o depliegues causaban pérdida de datos en el panel administrativo, fallas en la integridad referencial y rotura de la base de datos compartida por interactuar incorrectamente con los esquemas activos.

### **Solución Aplicada**
*   **Checkpoint Obligatorio:** Antes de realizar respaldos en SQLite, realizar checkpointing (`PRAGMA wal_checkpoint(TRUNCATE);`) para volcar transacciones WAL pendientes.
*   **Backups Estructurados:** Generar backups separados del esquema (`_schema.sql`) y de los datos completos (`_dump.sql`) para mayor flexibilidad.
*   **Script Multiplataforma:** Utilizar scripts de restauración nativos de Python (`restore_db.py`) que no requieran ejecutables del sistema operativo y que manejen la eliminación segura de archivos temporales (`-wal`, `-shm`) para evitar bases de datos corruptas en Windows (Desarrollador) o Linux (Producción).

---

## 6. Sincronización de Git, Desfase de Commits y Restricciones de Red de Sandbox

### **Error Detectado**
*   **Could not resolve host:** Intentar sincronizar el repositorio con GitHub (`git pull`, `git push`) desde la terminal del Agente de IA arroja errores de resolución DNS debido a las restricciones físicas de aislamiento y seguridad del sandbox (nsjail), bloqueando la subida a internet de los cambios del día.
*   **Non-Fast-Forward / Commits Desfasados:** La rama local del repositorio en la VM puede quedar detrás de la remota de GitHub (`origin/main`) si se realizan commits directamente en el remoto, bloqueando los intentos estándar de `git push` con errores de sincronización (ej: "delante X, detrás Y").

### **Solución Aplicada**
*   **Script de Sincronización Automatizada (`git_sync.sh`):** Se programó un script interactivo con colores y emojis en la raíz del repositorio (`git_sync.sh`) para ser ejecutado directamente en la máquina real de Ubuntu del usuario (que sí tiene resolución DNS activa).
*   **Integración por Rebase:** El script ejecuta de forma automática `git pull --rebase origin main` para descargar los commits desfasados de GitHub de forma limpia sin generar commits de "merge" innecesarios, re-aplicando los commits del día local sobre el remoto, y culminando con un `git push origin main` hacia la cuenta de César Lenin (`Cesarl01/OpenSwarm.git`).
*   **Manejo Dinámico de Remotos:** El script autodetecta la URL de origin y la corrige dinámicamente si no apunta a la cuenta personal de `Cesarl01`.

