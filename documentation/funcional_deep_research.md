# Manual Funcional: Deep Research Agent

## 1. Funcionalidad y Objetivo
El **Deep Research Agent** (Agente de Investigación Profunda) está diseñado para realizar búsquedas exhaustivas e inteligentes en la web en tiempo real. No se limita a búsquedas superficiales de Google, sino que realiza consultas recursivas, lee contenido completo de páginas web, extrae datos técnicos relevantes, contrasta fuentes y produce informes académicos y empresariales enriquecidos con citas reales.

*   **Objetivo:** Ahorrar horas de navegación al usuario, condensando información compleja y estructurándola de forma balanceada (ventajas, desventajas, tendencias y estado del arte).

---

## 2. Acceso y Permisos según el Rol

| Permiso / Capacidad | Administrador (César Lenin) | Desarrollador (Antigravity/Hermes) | Usuario Final / Invitado |
| :--- | :---: | :---: | :---: |
| **Configurar API de Búsqueda (Tavily/Serper)** | Sí | Sí | No |
| **Modificar Estructura de Reporte** | Sí | Sí | No |
| **Iniciar Investigaciones Web** | Sí | Sí | Sí |
| **Exportar Reporte a PDF/Word** | Sí | Sí (Via Docs Agent) | Sí |
| **Ver Sitios Web Bloqueados** | Sí | Sí | No |

### 2.1 Rol: Administrador
*   **Qué puede ver:** El reporte técnico estructurado y los enlaces a las fuentes consultadas.
*   **Acciones permitidas:** Solicitar investigaciones de mercado confidenciales, patentes o temas de tesis de maestría.

### 2.2 Rol: Desarrollador
*   **Qué puede ver:** Logs de llamadas a las APIs de búsqueda y el proceso de scraping de las herramientas.
*   **Acciones permitidas:** Ajustar los prompts de filtrado para evitar que el agente consuma demasiados tokens procesando páginas web ruidosas o de spam.

### 2.3 Rol: Usuario Final
*   **Qué puede ver:** El resumen de la investigación en su chat y descargar el informe resultante.
*   **Acciones permitidas:** Pedir aclaraciones de conceptos o búsquedas sencillas sobre un tema específico (ej. *"¿Qué es WeasyPrint y cómo se instala?"*).
