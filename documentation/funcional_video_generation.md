# Manual Funcional: Video Generation Agent

## 1. Funcionalidad y Objetivo
El **Video Generation Agent** (Agente de Generación de Video) es el especialista más avanzado en material multimedia de OpenSwarm. Coordina motores de video de frontera como **Sora** (OpenAI), **Veo** (Google) y **Seedance** (fal.ai) para producir clips de alta definición y realismo. Adicionalmente, cuenta con herramientas avanzadas para la post-producción local: combinar múltiples clips, redimensionar, añadir transiciones y sincronizar subtítulos y voces artificiales (`AddSubtitles`, `CombineImages`, `EditImage`, `GenerateImage`).

*   **Objetivo:** Automatizar la creación de videos de marketing, demostraciones de productos (demos) y animaciones explicativas sin requerir suites de edición tradicionales.

---

## 2. Acceso y Permisos según el Rol

| Permiso / Capacidad | Administrador (César Lenin) | Desarrollador (Antigravity/Hermes) | Usuario Final / Invitado |
| :--- | :---: | :---: | :---: |
| **Configurar API Sora / Veo** | Sí | Sí | No |
| **Generar Videos Completos (Post-producción)** | Sí | Sí | Sí (Bajo cuotas) |
| **Añadir Subtítulos y Combinar Tomas** | Sí | Sí (Automático) | No |
| **Descargar Archivos de Video** | Sí | Sí | Sí |
| **Monitorear Costo por Generación** | Sí | Sí | No |

### 2.1 Rol: Administrador
*   **Qué puede ver:** El video final editado, renderizado y listo para reproducir o publicar.
*   **Acciones permitidas:** Solicitar videos promocionales de Zentia, videos tutoriales sobre el uso del ERP Dynoflow o animaciones explicativas para exposiciones de tesis.

### 2.2 Rol: Desarrollador
*   **Qué puede ver:** Trazas de la biblioteca `moviepy` y `ffmpeg` al procesar clips locales, logs de codificación y consumos de fal.ai/OpenAI.
*   **Acciones permitidas:** Optimizar las funciones de procesamiento local en `CombineImages.py` y `AddSubtitles.py` para evitar fugas de memoria o cuelgues del sistema en la VM con 4GB de RAM.

### 2.3 Rol: Usuario Final
*   **Qué puede ver:** Un clip de video renderizado para reproducir.
*   **Acciones permitidas:** Generar videos cortos animados o instructivos breves (ej. *"crea una animación de un engrane giratorio moderno"*).
