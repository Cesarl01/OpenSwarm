# Manual Funcional: Image Generation Agent

## 1. Funcionalidad y Objetivo
El **Image Generation Agent** (Agente de Generación de Imágenes) está diseñado para concebir, refinar y editar recursos gráficos mediante inteligencia artificial. Utiliza modelos avanzados de última generación, incluyendo **Gemini Image** (para operaciones nativas integradas) y **fal.ai** (para imágenes hiperrealistas y arte conceptual). Tiene la capacidad de crear banners, mockups de interfaces de usuario (UI), logotipos y elementos ilustrativos para presentaciones.

*   **Objetivo:** Permitir la conceptualización visual autónoma de ideas de negocio, interfaces de sistemas o recursos gráficos premium sin depender de diseñadores externos.

---

## 2. Acceso y Permisos según el Rol

| Permiso / Capacidad | Administrador (César Lenin) | Desarrollador (Antigravity/Hermes) | Usuario Final / Invitado |
| :--- | :---: | :---: | :---: |
| **Configurar Claves de fal.ai / Google Cloud** | Sí | Sí | No |
| **Generar Imágenes Premium de Alta Resolución**| Sí | Sí | Sí (Bajo cuotas) |
| **Realizar Edición Inpainting / Outpainting** | Sí | Sí | No |
| **Descargar Archivos de Imagen** | Sí | Sí | Sí |
| **Modificar Parámetros de Estética base** | Sí | Sí | No |

### 2.1 Rol: Administrador
*   **Qué puede ver:** Las imágenes resultantes generadas en alta calidad para sus proyectos de Zentia o Dynoflow.
*   **Acciones permitidas:** Solicitar diseños de banners publicitarios, mockups de la interfaz móvil de condominios o esquemas de flujo atractivos.

### 2.2 Rol: Desarrollador
*   **Qué puede ver:** Logs de llamadas a la API de fal.ai, URLs de descarga temporales y parámetros estéticos (seed, sampler, aspect ratio).
*   **Acciones permitidas:** Ajustar los prompts por defecto de los agentes en `image_generation_agent/instructions.md` para garantizar que las imágenes tengan estilos pulidos, profesionales y de diseño corporativo moderno (evitando distorsiones o resultados de baja resolución).

### 2.3 Rol: Usuario Final
*   **Qué puede ver:** La imagen final renderizada directamente en su chat.
*   **Acciones permitidas:** Generar imágenes sencillas mediante descripciones de texto (ej. *"dibuja un gato robot programando en una laptop"*).
