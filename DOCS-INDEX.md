# 📚 Index de la Documentation

Guide complet de toute la documentation du projet.

## 🚀 Démarrage Rapide

- **[QUICK-START.md](./QUICK-START.md)** ⭐
  - Installation initiale
  - Workflow quotidien
  - Commandes essentielles
  - **Commencez par ici !**

## 📖 Documentation Principale

### Vue d'ensemble
- **[README.md](./README.md)**
  - Description du projet
  - Structure
  - Installation
  - API endpoints
  - Déploiement

### Développement
- **[DEVELOPMENT.md](./DEVELOPMENT.md)**
  - Guide de développement complet
  - Backend + Frontend
  - Workflow
  - Commandes
  - Qualité du code

## 🔧 Outils

### Pre-commit Hooks
- **[PRE-COMMIT.md](./PRE-COMMIT.md)**
  - Guide complet pre-commit
  - Installation
  - Configuration
  - Hooks disponibles
  - Troubleshooting

- **[PRE-COMMIT-SUMMARY.md](./PRE-COMMIT-SUMMARY.md)**
  - Résumé rapide
  - Avant/Après
  - Bénéfices

### Linting & Formatage
- **[TOOLS.md](./TOOLS.md)**
  - Ruff (Python)
  - ESLint + Prettier (TypeScript)
  - Comparaison
  - Configuration

## 📁 Documentation par composant

### Backend (Django)
- **[backend/README.md](./backend/README.md)**
  - Installation Django
  - API endpoints
  - Ruff usage
  - Structure

### Frontend (React)
- **[frontend/README.md](./frontend/README.md)**
  - Installation React
  - Structure des composants
  - ESLint + Prettier
  - Tests

## 🔍 Configuration

### Pre-commit
- **[.pre-commit-config.yaml](./.pre-commit-config.yaml)**
  - Configuration des hooks
  - Repos utilisés
  - Arguments

### Backend
- **[backend/ruff.toml](./backend/ruff.toml)**
  - Configuration Ruff
- **[backend/pyproject.toml](./backend/pyproject.toml)**
  - Métadonnées projet
- **[backend/.ruffignore](./backend/.ruffignore)**
  - Fichiers ignorés

### Frontend
- **[frontend/.eslintrc.json](./frontend/.eslintrc.json)**
  - Configuration ESLint
- **[frontend/.prettierrc.json](./frontend/.prettierrc.json)**
  - Configuration Prettier
- **[frontend/.prettierignore](./frontend/.prettierignore)**
  - Fichiers ignorés

### VSCode
- **[.vscode/settings.json](./.vscode/settings.json)**
  - Configuration IDE
- **[.vscode/extensions.json](./.vscode/extensions.json)**
  - Extensions recommandées

## 🧪 Tests et Scripts

- **[test-precommit.sh](./test-precommit.sh)**
  - Script de test des hooks
  - Exécutable : `./test-precommit.sh`

## 📦 Fichiers de dépendances

### Backend
- **[backend/requirements.txt](./backend/requirements.txt)**
  - Dépendances Python
  - Django, DRF, Ruff, etc.

### Frontend
- **[frontend/package.json](./frontend/package.json)**
  - Dépendances npm
  - Scripts disponibles

## 🎯 Makefiles

- **[backend/Makefile](./backend/Makefile)**
  - Commandes backend : lint, format, fix

- **[frontend/Makefile](./frontend/Makefile)**
  - Commandes frontend : lint, format, fix

## 🔗 Ordre de lecture recommandé

### Pour débuter (nouveau sur le projet)
1. **[README.md](./README.md)** - Vue d'ensemble
2. **[QUICK-START.md](./QUICK-START.md)** - Installation
3. **[PRE-COMMIT-SUMMARY.md](./PRE-COMMIT-SUMMARY.md)** - Workflow
4. **[DEVELOPMENT.md](./DEVELOPMENT.md)** - Développement

### Pour la configuration des outils
1. **[TOOLS.md](./TOOLS.md)** - Comprendre les outils
2. **[PRE-COMMIT.md](./PRE-COMMIT.md)** - Configuration détaillée
3. **[backend/README.md](./backend/README.md)** - Backend spécifique
4. **[frontend/README.md](./frontend/README.md)** - Frontend spécifique

### Pour le troubleshooting
1. **[PRE-COMMIT.md](./PRE-COMMIT.md)** - Section Troubleshooting
2. **[DEVELOPMENT.md](./DEVELOPMENT.md)** - Workflow
3. **[QUICK-START.md](./QUICK-START.md)** - Commandes de base

## 📊 Résumé des fichiers

```
Racine du projet
├── README.md                    # Vue d'ensemble
├── QUICK-START.md              # Démarrage rapide ⭐
├── DEVELOPMENT.md              # Guide développement
├── PRE-COMMIT.md               # Guide pre-commit complet
├── PRE-COMMIT-SUMMARY.md       # Résumé pre-commit
├── TOOLS.md                    # Détails outils
├── DOCS-INDEX.md               # Ce fichier
├── test-precommit.sh           # Script de test
├── .pre-commit-config.yaml     # Config pre-commit
├── .gitignore                  # Git ignore
│
├── .vscode/
│   ├── settings.json           # Config VSCode
│   └── extensions.json         # Extensions recommandées
│
├── backend/
│   ├── README.md               # Doc backend
│   ├── requirements.txt        # Dépendances Python
│   ├── Makefile               # Commandes backend
│   ├── ruff.toml              # Config Ruff
│   ├── pyproject.toml         # Métadonnées
│   └── .ruffignore            # Ruff ignore
│
└── frontend/
    ├── README.md              # Doc frontend
    ├── package.json           # Dépendances npm
    ├── Makefile              # Commandes frontend
    ├── .eslintrc.json        # Config ESLint
    ├── .prettierrc.json      # Config Prettier
    └── .prettierignore       # Prettier ignore
```

## 🎓 Par cas d'usage

### "Je viens d'arriver sur le projet"
→ **[QUICK-START.md](./QUICK-START.md)**

### "Comment formater mon code ?"
→ **[PRE-COMMIT-SUMMARY.md](./PRE-COMMIT-SUMMARY.md)**

### "Comment configurer les outils ?"
→ **[TOOLS.md](./TOOLS.md)** + **[PRE-COMMIT.md](./PRE-COMMIT.md)**

### "Ça ne marche pas !"
→ **[PRE-COMMIT.md](./PRE-COMMIT.md)** - Section Troubleshooting

### "Je veux tout comprendre"
→ Lire dans l'ordre :
1. README.md
2. QUICK-START.md
3. DEVELOPMENT.md
4. TOOLS.md
5. PRE-COMMIT.md

## 📝 Mettre à jour la documentation

Quand vous ajoutez un nouveau document :
1. Créer le fichier `.md`
2. L'ajouter dans ce fichier `DOCS-INDEX.md`
3. Le référencer dans `README.md` si pertinent

---

**📚 20+ fichiers de documentation**
**🎯 Guide complet du A à Z**
**✅ Tout est documenté !**
