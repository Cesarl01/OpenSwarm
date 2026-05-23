#!/usr/bin/env python3
"""
Script de restauración multiplataforma para bases de datos SQLite de Hermes (kanban.db y state.db).
Diseñado para funcionar sin dependencias externas tanto en Linux (Producción) como en Windows (Desarrollo).
Usa la biblioteca estándar de Python 'sqlite3' para máxima portabilidad y robustez.
"""

import os
import sys
import sqlite3
import argparse

# Configuración de rutas relativas
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# La raíz del proyecto Hermes está dos niveles arriba de este script si está en openswarm/database_backups/
HERMES_ROOT = os.path.dirname(os.path.dirname(BASE_DIR))

# Rutas de base de datos destino
DB_PATHS = {
    "kanban": os.path.join(HERMES_ROOT, "kanban.db"),
    "state": os.path.join(HERMES_ROOT, "state.db")
}

# Rutas de respaldos SQL
BACKUP_PATHS = {
    "kanban": os.path.join(BASE_DIR, "kanban_dump.sql"),
    "state": os.path.join(BASE_DIR, "state_dump.sql")
}

def restore_database(db_key, force=False):
    db_path = DB_PATHS[db_key]
    backup_path = BACKUP_PATHS[db_key]

    print(f"\n--- Restaurando Base de Datos: {db_key} ---")
    print(f"Archivo de Respaldo: {backup_path}")
    print(f"Base de Datos Destino: {db_path}")

    # Validar si el respaldo existe
    if not os.path.exists(backup_path):
        print(f"ERROR: No se encontró el archivo de respaldo {backup_path}", file=sys.stderr)
        return False

    # Validar si el destino ya existe
    if os.path.exists(db_path) and not force:
        print(f"ADVERTENCIA: La base de datos destino ya existe en '{db_path}'.")
        confirm = input("¿Desea sobreescribirla? Esto eliminará todos los datos actuales. (s/N): ")
        if confirm.lower() != 's':
            print("Restauración cancelada por el usuario.")
            return False

    try:
        # Si la base de datos destino ya existe, la eliminamos para hacer una restauración limpia
        if os.path.exists(db_path):
            os.remove(db_path)
            # También eliminamos archivos WAL/SHM si existen
            for ext in ['-wal', '-shm', '-journal']:
                extra_file = db_path + ext
                if os.path.exists(extra_file):
                    os.remove(extra_file)

        # Leer el archivo de volcado SQL
        print("Leyendo volcado SQL...")
        with open(backup_path, 'r', encoding='utf-8') as f:
            sql_script = f.read()

        # Conectar a la nueva base de datos y ejecutar el script SQL
        print("Restaurando estructura y datos en SQLite...")
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        
        # Ejecutar script completo
        cursor.executescript(sql_script)
        conn.commit()
        conn.close()

        print(f"ÉXITO: La base de datos '{db_key}' ha sido restaurada con éxito.")
        return True

    except Exception as e:
        print(f"ERROR al restaurar la base de datos: {e}", file=sys.stderr)
        return False

def main():
    parser = argparse.ArgumentParser(description="Restaurador multiplataforma de bases de datos para Hermes (Cybite Architecture)")
    parser.add_argument("--db", choices=["kanban", "state", "all"], default="all",
                        help="Base de datos a restaurar: 'kanban', 'state' o 'all' (por defecto: 'all')")
    parser.add_argument("--force", action="store_true",
                        help="Sobreescribe las bases de datos existentes sin solicitar confirmación")
    
    args = parser.parse_args()

    print("=====================================================================")
    print("      Restaurador de Base de Datos Hermes - Arquitectura Cybite      ")
    print("=====================================================================")
    print(f"Detectado Sistema Operativo: {os.name} ({sys.platform})")
    
    dbs_to_restore = []
    if args.db == "all":
        dbs_to_restore = ["kanban", "state"]
    else:
        dbs_to_restore = [args.db]

    success_count = 0
    for db in dbs_to_restore:
        if restore_database(db, force=args.force):
            success_count += 1

    print("\n=====================================================================")
    print(f"Proceso finalizado. {success_count} de {len(dbs_to_restore)} bases de datos restauradas.")
    print("=====================================================================")

if __name__ == "__main__":
    main()
