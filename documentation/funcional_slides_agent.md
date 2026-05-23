# Manual Funcional: Slides Agent

## 1. Funcionalidad y Objetivo
El **Slides Agent** (Agente de Diapositivas) se especializa en la estructuración, diseño y exportación de presentaciones. A diferencia de soluciones tradicionales que crean diapositivas simples y aburridas, este agente genera plantillas interactivas modernas basadas en HTML (usando Reveal.js o layouts CSS dinámicos de alto impacto visual) y luego las exporta al formato estándar de Microsoft PowerPoint (`.pptx`).

*   **Objetivo:** Permitir al usuario crear presentaciones profesionales y corporativas listas para exponer a partir de un simple bosquejo o una idea general.

---

## 2. Acceso y Permisos según el Rol

| Permiso / Capacidad | Administrador (César Lenin) | Desarrollador (Antigravity/Hermes) | Usuario Final / Invitado |
| :--- | :---: | :---: | :---: |
| **Definir Plantillas de Diseño (CSS)** | Sí | Sí | No |
| **Generar Nuevas Presentaciones** | Sí | Sí | Sí |
| **Descargar Archivos PPTX / HTML** | Sí | Sí | Sí |
| **Modificar Estructura de Secciones** | Sí | Sí | No (Solo vía prompt) |
| **Vincular Imágenes con Image Agent** | Sí | Sí (Automático) | No |

### 2.1 Rol: Administrador
*   **Qué puede ver:** La presentación generada tanto en la web/HTML como el archivo descargable de PowerPoint.
*   **Acciones permitidas:** Solicitar diapositivas ejecutivas para defensas de tesis de maestría, propuestas comerciales de Zentia o integraciones de Dynoflow.

### 2.2 Rol: Desarrollador
*   **Qué puede ver:** El código HTML/CSS intermedio y los logs de la biblioteca `python-pptx` durante la conversión de elementos.
*   **Acciones permitidas:** Modificar los estilos base del archivo `slide_html_utils.py` para asegurar que el diseño predeterminado cumpla con las directrices premium (colores modernos, tipografías elegantes, micro-animaciones).

### 2.3 Rol: Usuario Final
*   **Qué puede ver:** Un enlace de descarga de la presentación final y previsualizaciones de texto.
*   **Acciones permitidas:** Solicitar diapositivas sobre un tema específico (ej. *"crea una presentación sobre la historia de la IA"*).
