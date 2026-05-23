#!/usr/bin/env bash
# ==============================================================================
# Script de Sincronización Automatizada para OpenSwarm
# Diseñado para resolver desfases de commits y realizar push a GitHub (Cesarl01)
# ==============================================================================

# Colores para la consola
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # Sin color

echo -e "${BLUE}====================================================${NC}"
echo -e "${BLUE}🔄  Iniciando Sincronización Automática con GitHub${NC}"
echo -e "${BLUE}====================================================${NC}"

# 1. Verificar si estamos en el repositorio git correcto
if [ ! -d .git ]; then
    echo -e "${RED}❌ Error: Este script debe ejecutarse en la raíz del repositorio openswarm.${NC}"
    exit 1
fi

# 2. Mostrar la URL del repositorio remoto
REMOTE_URL=$(git remote get-url origin)
echo -e "${BLUE}📦 Repositorio remoto actual:${NC} ${YELLOW}${REMOTE_URL}${NC}"

if [[ ! "$REMOTE_URL" =~ "Cesarl01" ]]; then
    echo -e "${YELLOW}⚠️ Advertencia: El remoto 'origin' no apunta al usuario Cesarl01.${NC}"
    echo -e "${BLUE}🔧 Configurando origin a https://github.com/Cesarl01/OpenSwarm.git...${NC}"
    git remote set-url origin https://github.com/Cesarl01/OpenSwarm.git
    REMOTE_URL=$(git remote get-url origin)
    echo -e "${GREEN}✓ Remoto origin actualizado con éxito a: ${REMOTE_URL}${NC}"
fi

# 3. Descargar los metadatos más recientes de GitHub
echo -e "\n${BLUE}📥 1. Descargando cambios recientes desde GitHub (git fetch)...${NC}"
git fetch origin main

# 4. Verificar desfase de commits
LOCAL_COMMIT=$(git rev-parse HEAD)
REMOTE_COMMIT=$(git rev-parse origin/main)

if [ "$LOCAL_COMMIT" = "$REMOTE_COMMIT" ]; then
    echo -e "${GREEN}✓ El repositorio ya está perfectamente sincronizado con GitHub.${NC}"
    exit 0
fi

# Calcular cuántos commits de diferencia hay
BEHIND=$(git rev-list --count HEAD..origin/main)
AHEAD=$(git rev-list --count origin/main..HEAD)

echo -e "${YELLOW}📊 Estado de la rama local respecto a origin/main:${NC}"
echo -e "   - Commits locales por subir (Ahead): ${GREEN}${AHEAD}${NC}"
echo -e "   - Commits remotos por descargar (Behind): ${RED}${BEHIND}${NC}"

# 5. Integrar cambios remotos usando rebase para evitar commits de merge sucios
echo -e "\n${BLUE}🔄 2. Integrando cambios remotos de forma limpia (git pull --rebase)...${NC}"
git pull --rebase origin main

if [ $? -ne 0 ]; then
    echo -e "${RED}❌ Error durante el rebase. Es posible que existan conflictos.${NC}"
    echo -e "${YELLOW}💡 Si hay conflictos, resuélvelos y ejecuta 'git rebase --continue'.${NC}"
    echo -e "${YELLOW}   O puedes abortar la operación con 'git rebase --abort'.${NC}"
    exit 1
fi
echo -e "${GREEN}✓ Cambios remotos integrados exitosamente. Tu código local está al día.${NC}"

# 6. Subir los cambios finales a GitHub
echo -e "\n${BLUE}📤 3. Subiendo todos los cambios al repositorio de Cesarl01...${NC}"
git push origin main

if [ $? -ne 0 ]; then
    echo -e "${RED}❌ Error: No se pudieron subir los cambios a GitHub.${NC}"
    echo -e "${YELLOW}👉 Verifica que tu clave SSH o Token de GitHub tengan permisos de escritura en Cesarl01/OpenSwarm.${NC}"
    exit 1
fi

echo -e "\n${GREEN}====================================================${NC}"
echo -e "${GREEN}🎉 ¡ÉXITO! Todos los cambios han sido subidos a GitHub.${NC}"
echo -e "${GREEN}📂 Repositorio: https://github.com/Cesarl01/OpenSwarm.git${NC}"
echo -e "${GREEN}====================================================${NC}"
