#!/bin/bash

echo "🧪 Test des pre-commit hooks"
echo ""
echo "Ce script teste que les hooks pre-commit fonctionnent correctement."
echo ""

# Couleurs
GREEN='\033[0;32m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

echo -e "${BLUE}1. Vérification de l'installation...${NC}"
if command -v pre-commit &> /dev/null; then
    echo "✅ pre-commit est installé"
else
    echo "❌ pre-commit n'est pas installé"
    echo "   Installer avec: pip install pre-commit"
    exit 1
fi

echo ""
echo -e "${BLUE}2. Test des hooks sur tous les fichiers...${NC}"
pre-commit run --all-files

if [ $? -eq 0 ]; then
    echo ""
    echo -e "${GREEN}✅ Tous les hooks ont réussi !${NC}"
    echo ""
    echo "Les hooks pre-commit sont configurés et fonctionnent correctement."
    echo "Ils s'exécuteront automatiquement avant chaque commit."
else
    echo ""
    echo "⚠️  Certains hooks ont échoué ou modifié des fichiers."
    echo "C'est normal ! Les fichiers ont été corrigés automatiquement."
    echo "Lancez à nouveau pour vérifier : pre-commit run --all-files"
fi
