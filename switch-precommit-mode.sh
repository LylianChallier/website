#!/bin/bash

# Script pour changer le mode pre-commit

GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
NC='\033[0m'

echo -e "${BLUE}🔧 Changement de mode pre-commit${NC}"
echo ""
echo "Modes disponibles:"
echo "  1) Souple (soft) - Auto-fix mais ne bloque jamais [ACTUEL]"
echo "  2) Strict - Bloque le commit si erreurs"
echo "  3) Minimal - Seulement formatage, pas de checks"
echo "  4) Désactiver - Aucun hook"
echo ""
read -p "Choisir un mode (1-4): " mode

case $mode in
  1)
    if [ -f ".pre-commit-config.yaml" ]; then
      echo -e "${YELLOW}Mode souple déjà actif${NC}"
    else
      echo -e "${GREEN}✓ Mode souple activé${NC}"
      git mv .pre-commit-config-*.yaml .pre-commit-config.yaml 2>/dev/null || true
    fi
    ;;
  2)
    mv .pre-commit-config.yaml .pre-commit-config-soft.yaml
    mv .pre-commit-config-strict.yaml .pre-commit-config.yaml
    echo -e "${GREEN}✓ Mode strict activé (bloque les commits)${NC}"
    ;;
  3)
    mv .pre-commit-config.yaml .pre-commit-config-soft.yaml
    mv .pre-commit-config-minimal.yaml .pre-commit-config.yaml
    echo -e "${GREEN}✓ Mode minimal activé (formatage seulement)${NC}"
    ;;
  4)
    pre-commit uninstall
    echo -e "${YELLOW}✓ Pre-commit désactivé${NC}"
    echo "Pour réactiver: pre-commit install"
    exit 0
    ;;
  *)
    echo -e "${YELLOW}Choix invalide${NC}"
    exit 1
    ;;
esac

# Réinstaller les hooks
pre-commit install --overwrite

echo ""
echo -e "${GREEN}Configuration mise à jour !${NC}"
echo "Test: pre-commit run --all-files"
