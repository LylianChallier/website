# Quick Start

Guide de démarrage rapide pour le projet Portfolio Django + React.

## Installation initiale (une seule fois)

### 1. Backend Django

```bash
cd backend
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
```

### 2. Frontend React

```bash
cd frontend
npm install
```

### 3. Pre-commit Hooks

```bash
cd ..  # Retour à la racine du projet
pip install pre-commit
pre-commit install
```

✅ **C'est tout !** Les hooks pre-commit sont maintenant actifs.

## Développement quotidien

### Lancer les serveurs

**Terminal 1 - Backend :**
```bash
cd backend
source venv/bin/activate
python manage.py runserver
# API sur http://localhost:8000
```

**Terminal 2 - Frontend :**
```bash
cd frontend
npm start
# App sur http://localhost:3000
```

### Workflow Git

```bash
# Faire des modifications dans le code
# ...

# Stagé les fichiers
git add .

# Commit (les hooks s'exécutent automatiquement)
git commit -m "Description des changements"
# ⚡ Ruff, ESLint, Prettier s'exécutent automatiquement
# ✅ Si tout passe, le commit est créé
# ⚠️  Si des fichiers sont modifiés, re-stagé et recommit

# Push
git push
```

**C'est tout !** Plus besoin de lancer manuellement `make lint` ou `make format`.

## Workflow complet exemple

```bash
# 1. Modifier du code Python
vim backend/core/views.py

# 2. Modifier du code React
vim frontend/src/App.tsx

# 3. Commit
git add .
git commit -m "Add new feature"

# Les hooks s'exécutent automatiquement :
# ✓ Ruff lint backend
# ✓ Ruff format backend
# ✓ ESLint frontend
# ✓ Prettier frontend
# ✓ Trailing whitespace
# ✓ End of file
# ✓ Check JSON
# ✓ Mixed line endings

# Si tout passe : commit créé ✅
# Si corrections nécessaires : fichiers modifiés automatiquement
#   → git add . && git commit -m "Add new feature"

# 4. Push
git push
```

## Commandes utiles

### Tests manuels (optionnel)

```bash
# Tester tous les hooks sans commiter
pre-commit run --all-files

# Backend uniquement
cd backend && make fix

# Frontend uniquement
cd frontend && make fix
```

### Bypass (urgence uniquement)

```bash
# Bypasser les hooks (déconseillé)
git commit --no-verify -m "Emergency fix"
```

## Structure des commandes

```
Racine du projet
├── pre-commit run --all-files    # Tout tester
│
├── backend/
│   ├── make lint                 # Ruff check
│   ├── make format               # Ruff format
│   └── make fix                  # Lint + format
│
└── frontend/
    ├── make lint                 # ESLint
    ├── make format               # Prettier
    └── make fix                  # Lint + format
```

## Troubleshooting

### Les hooks ne s'exécutent pas

```bash
pre-commit install
```

### Erreur lors du commit

```bash
# Re-stagé les fichiers corrigés
git add .
git commit -m "Votre message"
```

### Réinstaller les hooks

```bash
pre-commit clean
pre-commit install --install-hooks
```

## Ce qui est automatisé

✅ **Backend Python :**
- Formatage du code (Ruff)
- Tri des imports (Ruff)
- Correction des erreurs de style (Ruff)
- Vérification PEP 8

✅ **Frontend TypeScript/React :**
- Formatage du code (Prettier)
- Correction des erreurs ESLint
- Organisation du code

✅ **Fichiers généraux :**
- Suppression espaces en fin de ligne
- Ligne vide en fin de fichier
- Normalisation des fins de ligne (LF)
- Vérification JSON/YAML
- Détection de gros fichiers

## Documentation complète

- [README.md](./README.md) - Vue d'ensemble
- [PRE-COMMIT.md](./PRE-COMMIT.md) - Guide pre-commit détaillé
- [DEVELOPMENT.md](./DEVELOPMENT.md) - Guide de développement
- [TOOLS.md](./TOOLS.md) - Détails des outils

## En résumé

**Avant :**
```bash
# Workflow manuel
git add .
cd backend && make fix
cd ../frontend && make fix
cd ..
git commit -m "Message"
```

**Maintenant :**
```bash
# Workflow automatique
git add .
git commit -m "Message"
# ✨ Tout est fait automatiquement !
```

**Gain de temps : ~30 secondes par commit** ⚡
