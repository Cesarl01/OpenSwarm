# Manual de Usuario - Sistema Inteligente Hermes & OpenSwarm

¡Bienvenido a **Hermes & OpenSwarm**! Este sistema es tu equipo de trabajo digital y autónomo, diseñado para automatizar la gestión de conocimiento, realizar investigaciones profundas, estructurar datos y generar entregables de nivel ejecutivo directamente desde tus instrucciones en lenguaje natural.

---

## 1. ¿Cómo interactuar con Hermes?

Puedes interactuar con Hermes principalmente de dos maneras: **vía chat de Telegram** o a través de **comandos en la terminal**.

### 1.1 Interacción por Telegram (Tu Asistente de Bolsillo)
Hermes te acompaña en tu teléfono o computadora a través de Telegram. 
*   **Conversación Fluida:** Escríbele o envíale notas de voz en español como lo harías con un colega de trabajo.
*   **Gestión Kanban:** Puedes pedirle que administre tus tareas. Por ejemplo:
    *   *"Crea una tarea para investigar los competidores de Zentia"*
    *   *"Muéstrame las tareas pendientes de hoy"*
    *   *"Marca la tarea de respaldo de base de datos como completada"*
*   **Respuestas Inteligentes sin Truncamiento:** Si le pides a Hermes un informe muy largo, el sistema lo dividirá automáticamente en fragmentos ordenados para que no se pierda información debido a los límites de Telegram.

---

## 2. Búsqueda y Manejo Autónomo de Google Drive

Una de las capacidades más potentes de Hermes es su integración con tu Google Drive sin que tengas que lidiar con IDs largos o complejos de carpetas. **Tú hablas en lenguaje natural, Hermes hace el trabajo técnico en segundo plano.**

### 2.1 Búsqueda Autónoma de Archivos
*   **Cómo pedirlo:** Simplemente di: *"Busca el manual de OpenSwarm en la carpeta compartida"* o *"Lista los archivos de la tesis"*.
*   **Ejecución Silenciosa:** Hermes buscará el archivo en segundo plano sin pedirte enlaces.
*   **Lista Numerada Inteligente:** Hermes te presentará una lista limpia, por ejemplo:
    1.  `Tesis_Maestria_Borrador_V2.docx`
    2.  `Manual_OpenSwarm_Instalacion.pdf`
    3.  `Video_Demostración_Zentia.mp4`
*   **Cómo actuar sobre la lista:** Si quieres que analice el primer archivo, solo di: *"Analiza el archivo 1"* o *"Haz un resumen del borrador de la tesis"*. Hermes recordará qué ID corresponde a ese número y lo procesará automáticamente.

### 2.2 Transcripción y Análisis de Videos Gratuitos
Si tienes un video en Google Drive (como grabaciones de tus clases de maestría o demos de sistemas):
*   Pídele: *"Transcribe el video de la tesis"* o *"Haz una bitácora del video 3"*.
*   Hermes descargará el video, ejecutará el transcriptor local de forma 100% gratuita y te entregará:
    1.  Una **bitácora temporal** detallada (minuto a minuto de lo que se habla).
    2.  Un **resumen ejecutivo** estructurado en español.

---

## 3. Delegación de Tareas Especialistas (OpenSwarm)

Cuando necesitas un trabajo pesado o un entregable formal, Hermes delega la tarea a un equipo de agentes especialistas autónomos (OpenSwarm). 

Solo debes pedirle a Hermes lo que necesitas y él coordinará al especialista adecuado:

### 3.1 Crear Presentaciones de Diapositivas (Slides Agent)
*   **Instrucción:** *"Genera una presentación comercial para captar inversores en OpenSwarm"*
*   **Entregable:** El sistema creará un conjunto de diapositivas interactivas en HTML con un diseño moderno y las exportará a formato PowerPoint (`.pptx`) para que las descargues listas para usar.

### 3.2 Crear Informes y Documentos PDF / Word (Docs Agent)
*   **Instrucción:** *"Redacta un informe técnico completo de la Arquitectura Cybite y compártelo en formato PDF"*
*   **Entregable:** Un archivo formateado profesionalmente con índice, títulos limpios y tablas estructuradas.

### 3.3 Análisis de Datos y Gráficos (Data Analyst Agent)
*   **Instrucción:** *"Analiza este archivo CSV de ventas, haz una regresión estadística y genera un gráfico de tendencias"*
*   **Entregable:** Un reporte detallado con las conclusiones matemáticas y las imágenes de los gráficos guardadas para que las descargues.

### 3.4 Investigaciones Web Exhaustivas (Deep Research Agent)
*   **Instrucción:** *"Realiza una investigación exhaustiva sobre las últimas tendencias en RAG y Gemini 2.5 en 2026"*
*   **Entregable:** Un reporte académico robusto con citas web reales, pros y contras de cada tecnología y un análisis estratégico.

---

## 4. Rutinas de Cierre de Tareas (`/end-daily`)

Al finalizar tu jornada laboral o tu día de desarrollo, puedes ordenar una rutina de mantenimiento completa escribiendo:
`@[/end-daily]` o *"Ejecuta el cierre del día"*.

Esto disparará de forma autónoma:
1.  **Respaldo de Base de Datos:** Guardará de manera consistente todos tus tableros kanban y estados conversacionales en el repositorio.
2.  **Actualización de Manuales:** Asegura que todos los documentos de soporte técnico y de usuario estén actualizados.
3.  **Actualización de Código (Git):** Limpiará el código de archivos temporales e innecesarios y subirá los cambios directamente a tu GitHub de manera ordenada.
4.  **Cierre de Tareas:** Dará por concluidas las actividades del día en el registro del Kanban.
