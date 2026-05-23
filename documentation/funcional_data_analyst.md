# Manual Funcional: Data Analyst Agent

## 1. Funcionalidad y Objetivo
El **Data Analyst Agent** (Agente Analista de Datos) está diseñado para realizar tareas complejas de manipulación y análisis estadístico de datos en un entorno seguro y aislado. Utiliza una herramienta de interpretación de código en Python (`IPythonInterpreter`) para cargar archivos CSV, Excel o bases de datos SQLite y Postgres, limpiar registros, ejecutar modelos estadísticos y graficar los resultados.

*   **Objetivo:** Proporcionar un científico de datos autónomo capaz de extraer conocimiento de datasets crudos y generar visualizaciones claras de manera rápida y sin errores.

---

## 2. Acceso y Permisos según el Rol

| Permiso / Capacidad | Administrador (César Lenin) | Desarrollador (Antigravity/Hermes) | Usuario Final / Invitado |
| :--- | :---: | :---: | :---: |
| **Acceso a Bases de Datos de Producción** | Sí (Controlado) | Sí (Permiso explícito) | No |
| **Cargar Archivos CSV/Excel** | Sí | Sí | Sí |
| **Ejecutar Código de Consola Python** | Sí (Directo) | Sí (Aislado) | No (Solo vía prompt) |
| **Visualizar Gráficos Generados** | Sí | Sí | Sí |
| **Modificar Entorno Virtual de Ejecución** | Sí | Sí | No |

### 2.1 Rol: Administrador
*   **Qué puede ver:** El flujo de ejecución del código Python, las tablas de datos procesadas y los gráficos generados (gráficos de barras, dispersión, regresiones).
*   **Acciones permitidas:** Solicitar análisis sobre bases de datos de producción (ej. Zentia o Dynoflow), cruzar tablas y exportar reportes de negocio.

### 2.2 Rol: Desarrollador
*   **Qué puede ver:** Logs de la consola interactiva de IPython y errores de importación de librerías (pandas, numpy, seaborn, scikit-learn).
*   **Acciones permitidas:** Actualizar dependencias científicas en el entorno de OpenSwarm y corregir el manejo de memoria en scripts de carga.

### 2.3 Rol: Usuario Final
*   **Qué puede ver:** Gráficos estáticos e interpretaciones explicativas en español de las tendencias de los datos.
*   **Acciones permitidas:** Cargar su propia hoja de cálculo (ej. *"analiza este listado de gastos"*) y pedir promedios, tendencias o agrupaciones.
