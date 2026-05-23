# Manual Funcional: Virtual Assistant

## 1. Funcionalidad y Objetivo
El **Virtual Assistant** (Asistente Virtual) es el agente encargado de tareas administrativas diarias y de la interacción directa con servicios de terceros. A través de la integración con **Composio**, el Asistente Virtual tiene la capacidad de conectarse a más de 10,000 aplicaciones y herramientas (como Gmail, Google Calendar, Slack, Jira y GitHub).

*   **Objetivo:** Automatizar tareas rutinarias de oficina, redactar correos, gestionar calendarios, crear incidencias y coordinar flujos de trabajo de baja complejidad técnica.

---

## 2. Acceso y Permisos según el Rol

| Permiso / Capacidad | Administrador (César Lenin) | Desarrollador (Antigravity/Hermes) | Usuario Final / Invitado |
| :--- | :---: | :---: | :---: |
| **Vincular Cuentas de Composio** | Sí (Control total) | No (Solo uso) | No |
| **Leer/Enviar Correos y Calendario** | Sí | Sí (Bajo directiva) | No |
| **Gestionar Notificaciones** | Sí | Sí | No |
| **Ejecutar Herramientas Locales** | Sí | Sí | Sí (Restringido) |
| **Consultar Historial de Tareas** | Sí | Sí | Sí |

### 2.1 Rol: Administrador
*   **Qué puede ver:** Todas las conexiones autorizadas en Composio y las acciones ejecutadas en sus plataformas personales (calendarios, chats).
*   **Acciones permitidas:** Autorizar nuevos tokens, revocar accesos de API y parametrizar recordatorios automáticos.

### 2.2 Rol: Desarrollador
*   **Qué puede ver:** Logs de llamadas a la API de Composio y payloads de respuesta de herramientas.
*   **Acciones permitidas:** Actualizar la lista de herramientas en `virtual_assistant/tools/` y depurar fallas de autenticación.

### 2.3 Rol: Usuario Final
*   **Qué puede ver:** Estado de sus recordatorios o respuestas enviadas en su chat.
*   **Acciones permitidas:** Solicitar agendamiento de reuniones o redacción de notas rápidas.
