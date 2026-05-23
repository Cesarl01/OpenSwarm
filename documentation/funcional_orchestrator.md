# Manual Funcional: Orchestrator Agent

## 1. Funcionalidad y Objetivo
El **Orchestrator Agent** (Agente Orquestador) es el núcleo de control del sistema de multi-agentes de OpenSwarm. No ejecuta tareas directamente ni genera archivos finales, sino que actúa como un enrutador inteligente de alta precisión. Analiza la solicitud inicial del usuario, identifica qué agentes especialistas son necesarios, desglosa la tarea en subtareas secuenciales o paralelas y coordina el flujo de trabajo final.

*   **Objetivo:** Garantizar que cada solicitud del usuario sea atendida por el especialista adecuado sin fricciones ni sobrecarga de procesamiento, administrando eficientemente los tokens y llamadas de API.

---

## 2. Acceso y Permisos según el Rol

| Permiso / Capacidad | Administrador (César Lenin) | Desarrollador (Antigravity/Hermes) | Usuario Final / Invitado |
| :--- | :---: | :---: | :---: |
| **Visualizar Logs de Enrutamiento** | Sí (Completo) | Sí (Acceso a debug) | No |
| **Configurar Modelos Core** | Sí | Sí | No |
| **Enviar Instrucciones de Enrutamiento** | Sí | Sí (Mediante API/Puente) | Sí |
| **Modificar Reglas de Negocio** | Sí | Sí | No |
| **Ejecutar fallback de agentes** | Sí (Automático) | Sí (Control de excepciones) | No |

### 2.1 Rol: Administrador
*   **Qué puede ver:** La traza completa de cómo el Orquestador desglosa sus solicitudes y delega a otros agentes.
*   **Acciones permitidas:** Cambiar el modelo de lenguaje del Orquestador (ej. Gemini vs Llama) en `config.py` o anular decisiones de enrutamiento.

### 2.2 Rol: Desarrollador
*   **Qué puede ver:** Logs detallados de tiempo de respuesta, tokens consumidos y llamadas a la clase `Agency` en `swarm.py`.
*   **Acciones permitidas:** Modificar las instrucciones en `orchestrator/instructions.md` para ajustar el comportamiento del Orquestador.

### 2.3 Rol: Usuario Final
*   **Qué puede ver:** El resultado final unificado de su solicitud. No ve la "cocina" interna del enrutamiento a menos que ocurra un error de sistema.
*   **Acciones permitidas:** Enviar instrucciones simples en lenguaje natural (ej. *"Haz una presentación comercial y busca datos"*).
