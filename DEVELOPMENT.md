# Guide de développement

Ce document décrit les outils et commandes pour le développement du projet.

## Structure du projet

```
website/
├── backend/          # Django + DRF
│   ├── mysite/       # Configuration
│   ├── core/         # App principale
│   ├── ruff.toml     # Config Ruff
│   └── Makefile      # Commandes pratiques
├── frontend/         # React + TypeScript
│   ├── src/
│   ├── .eslintrc.json
│   ├── .prettierrc.json
│   └── Makefile      # Commandes pratiques
└── .vscode/          # Configuration VSCode
    ├── settings.json
    └── extensions.json
```

## Backend (Django)

### Installation

```bash
cd backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
```

### Développement

```bash
python manage.py runserver
# API disponible sur http://localhost:8000
```

### Linting & Formatage avec Ruff

```bash
# Vérifier le code
make lint
# ou
ruff check .

# Formater le code
make format
# ou
ruff format .

# Tout corriger automatiquement
make fix
```

### Configuration Ruff

- **Fichier** : `backend/ruff.toml`
- **Règles** : pycodestyle, pyflakes, isort, pep8-naming, flake8-django
- **Longueur de ligne** : 88 caractères
- **Exclusions** : migrations, venv, staticfiles

## Frontend (React)

### Installation

```bash
cd frontend
npm install
```

### Développement

```bash
npm start
# ou
make dev
# Application disponible sur http://localhost:3000
```

### Linting & Formatage

```bash
# ESLint
npm run lint
make lint

# Prettier
npm run format
make format

# Tout corriger
make fix
```

### Configuration

- **ESLint** : `.eslintrc.json` - Vérification du code
- **Prettier** : `.prettierrc.json` - Formatage du code
- **Style** : Single quotes, 2 espaces, semicolons

## VSCode

### Extensions recommandées

Le fichier `.vscode/extensions.json` suggère :
- **ESLint** - Linting JavaScript/TypeScript
- **Prettier** - Formatage (optionnel, npm run format suffit)
- **Python** - Support Python
- **Ruff** - Linting & formatage Python

### Configuration

Le fichier `.vscode/settings.json` configure :
- **Python** : Ruff pour le formatage et linting
- **TypeScript/React** : ESLint actif
- **Formatage** : Via commandes npm/make (pas automatique)

## Workflow de développement

### Backend

1. Activer l'environnement virtuel
2. Modifier le code
3. Vérifier avec `make lint`
4. Formater avec `make format`
5. Tester l'API

### Frontend

1. Modifier le code
2. ESLint corrige automatiquement les erreurs basiques
3. Formater avec `make format`
4. Vérifier avec `make lint`
5. Tester dans le navigateur

## Commandes rapides

### Backend
```bash
cd backend
make fix          # Lint + format
make check        # Vérifier sans modifier
python manage.py runserver
```

### Frontend
```bash
cd frontend
make fix          # Lint + format
make check        # Vérifier sans modifier
make dev          # Lancer le dev server
make build        # Build de production
```

## Qualité du code

### Backend (Python)
- ✅ PEP 8 compliant
- ✅ Django best practices
- ✅ Imports triés automatiquement
- ✅ Type hints recommandés

### Frontend (TypeScript)
- ✅ TypeScript strict
- ✅ React hooks best practices
- ✅ Code formaté uniformément
- ✅ ESLint warnings minimaux

## Déploiement

### Backend
```bash
cd backend
pip install -r requirements.txt
python manage.py migrate
python manage.py collectstatic
gunicorn mysite.wsgi:application
```

### Frontend
```bash
cd frontend
npm run build
# Servir le dossier build/
```

## Ressources

- [Django REST Framework](https://www.django-rest-framework.org/)
- [Ruff Documentation](https://docs.astral.sh/ruff/)
- [React Documentation](https://react.dev/)
- [ESLint Rules](https://eslint.org/docs/rules/)
- [Prettier Options](https://prettier.io/docs/en/options.html)
