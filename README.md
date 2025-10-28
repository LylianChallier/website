# Portfolio Lylian Challier - Django + React

Application web portfolio convertie de HTML/CSS/JS vers Django (backend) + React (frontend).

## Structure du projet

```
website/
├── backend/          # Backend Django
│   ├── mysite/       # Configuration Django
│   ├── core/         # Application principale
│   ├── media/        # Fichiers médias (CV, etc.)
│   └── manage.py
├── frontend/         # Frontend React
│   ├── public/
│   ├── src/
│   │   ├── components/
│   │   ├── api.ts
│   │   ├── i18n.ts
│   │   └── types.ts
│   └── package.json
```

## Installation

### Backend (Django)

1. Créer un environnement virtuel :
```bash
cd backend
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

Le backend sera accessible sur `http://localhost:8000`

### Frontend (React)

1. Installer les dépendances :
```bash
cd frontend
npm install
```

2. Lancer le serveur de développement :
```bash
npm start
```

Le frontend sera accessible sur `http://localhost:3000`

## Fonctionnalités

- **API REST** : Django REST Framework pour servir les données du portfolio
- **Multilingue** : Support français/anglais avec i18next
- **Animations** : Animations au scroll et au chargement préservées
- **Responsive** : Design adaptatif conservé
- **TypeScript** : Frontend typé pour plus de sécurité
- **Qualité du code** : Ruff (Python) + ESLint/Prettier (TypeScript)

## API Endpoints

- `GET /api/portfolio/?lang=fr` : Récupère les données du portfolio en français
- `GET /api/portfolio/?lang=en` : Récupère les données du portfolio en anglais

## Déploiement

Pour le déploiement en production :

1. **Backend** :
   - Configurer `DEBUG = False` dans settings.py
   - Définir `ALLOWED_HOSTS` appropriés
   - Utiliser une base de données PostgreSQL
   - Configurer les fichiers statiques avec WhiteNoise ou serveur web

2. **Frontend** :
   - Build de production : `npm run build`
   - Déployer sur Netlify, Vercel ou servir via Django

## Développement

Les styles CSS originaux ont été préservés et les animations JavaScript ont été converties en animations React natives.

Le changement de langue met à jour dynamiquement le contenu via l'API Django.

### Linting & Formatage

#### Backend (Python avec Ruff)
```bash
cd backend
make lint      # Vérifier le code
make format    # Formater le code
make fix       # Corriger automatiquement
```

#### Frontend (TypeScript avec ESLint/Prettier)
```bash
cd frontend
make lint      # Vérifier avec ESLint
make format    # Formater avec Prettier
make fix       # Corriger et formater
```

Voir [DEVELOPMENT.md](./DEVELOPMENT.md) pour plus de détails.
