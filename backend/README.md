# Backend Django - Portfolio

Backend API REST pour le portfolio avec Django REST Framework.

## Installation

1. Créer un environnement virtuel :
```bash
python -m venv venv
source venv/bin/activate  # Sur Windows: venv\Scripts\activate
```

2. Installer les dépendances :
```bash
pip install -r requirements.txt
```

3. Effectuer les migrations :
```bash
python manage.py migrate
```

4. Lancer le serveur :
```bash
python manage.py runserver
```

## Linting et formatage avec Ruff

Ruff est un linter et formateur Python ultra-rapide, combinant les fonctionnalités de :
- Flake8
- isort
- Black
- pyupgrade
- et plus encore

### Commandes disponibles

```bash
# Vérifier le code (linting)
ruff check .

# Formater le code
ruff format .

# Corriger automatiquement les erreurs
ruff check --fix .

# Vérifier sans modifier
ruff format --check .
```

### Utilisation avec Make

```bash
make lint      # Vérifier le code
make format    # Formater le code
make check     # Lint + format check
make fix       # Corriger et formater automatiquement
```

### Configuration

La configuration Ruff se trouve dans :
- `ruff.toml` - Configuration principale
- `pyproject.toml` - Configuration alternative
- `.ruffignore` - Fichiers à ignorer

### Extension VSCode

Pour une intégration VSCode optimale :
1. Installez l'extension "Ruff" (charliermarsh.ruff)
2. La configuration est déjà dans `.vscode/settings.json`
3. Le formatage automatique à la sauvegarde est activé

## API Endpoints

- `GET /api/portfolio/?lang=fr` - Portfolio en français
- `GET /api/portfolio/?lang=en` - Portfolio en anglais

## Structure

```
backend/
├── mysite/         # Configuration Django
├── core/           # Application principale
│   ├── views.py    # Vues API
│   ├── serializers.py
│   ├── urls.py
│   └── models.py
├── requirements.txt
├── ruff.toml       # Config Ruff
└── manage.py
```
