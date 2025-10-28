# Outils de développement

Récapitulatif des outils de linting et formatage configurés dans le projet.

## Backend : Ruff

**Ruff** est un linter et formateur Python ultra-rapide qui remplace :
- Black (formatage)
- isort (tri des imports)
- Flake8 (linting)
- pyupgrade (modernisation du code)

### Configuration

- **Fichier principal** : `backend/ruff.toml`
- **Alternative** : `backend/pyproject.toml`
- **Exclusions** : `backend/.ruffignore`

### Règles activées

- `E` - Erreurs pycodestyle
- `W` - Warnings pycodestyle
- `F` - pyflakes (imports non utilisés, etc.)
- `I` - isort (tri des imports)
- `N` - pep8-naming (conventions de nommage)
- `UP` - pyupgrade (syntaxe moderne)
- `B` - flake8-bugbear (bugs courants)
- `C4` - flake8-comprehensions (optimisations)
- `DJ` - flake8-django (best practices Django)
- `SIM` - flake8-simplify (simplifications)

### Commandes

```bash
cd backend

# Vérifier
ruff check .
make lint

# Formater
ruff format .
make format

# Tout corriger
make fix
```

## Frontend : ESLint + Prettier

### ESLint

**ESLint** vérifie la qualité du code TypeScript/React.

- **Configuration** : `frontend/.eslintrc.json`
- **Extends** : react-app, prettier
- **Règles** :
  - Prettier warnings
  - No console (sauf warn/error)

```bash
cd frontend

# Vérifier
npm run lint
make lint

# Corriger automatiquement
npm run lint:fix
```

### Prettier

**Prettier** formate le code de manière consistante.

- **Configuration** : `frontend/.prettierrc.json`
- **Style** :
  - Single quotes
  - Semicolons
  - 2 espaces
  - 80 caractères max
  - Trailing commas ES5

```bash
cd frontend

# Formater
npm run format
make format

# Vérifier sans modifier
npm run format:check
```

## VSCode

### Extensions recommandées

Le fichier `.vscode/extensions.json` liste les extensions utiles :

```json
{
  "recommendations": [
    "dbaeumer.vscode-eslint",     // ESLint
    "esbenp.prettier-vscode",     // Prettier (optionnel)
    "ms-python.python",           // Python
    "charliermarsh.ruff"          // Ruff
  ]
}
```

### Configuration

Le fichier `.vscode/settings.json` configure :

**Python :**
- Ruff comme formateur
- Formatage automatique à la sauvegarde
- Organisation des imports automatique

**TypeScript/React :**
- ESLint actif
- Correction automatique à la sauvegarde
- Formatage via `npm run format` (manuel)

## Workflow recommandé

### Avant chaque commit

```bash
# Backend
cd backend
make fix

# Frontend
cd frontend
make fix
```

### CI/CD

Ajouter dans votre pipeline :

```yaml
# Backend
- name: Lint Python
  run: |
    cd backend
    ruff check .
    ruff format --check .

# Frontend
- name: Lint TypeScript
  run: |
    cd frontend
    npm run lint
    npm run format:check
```

## Comparaison

| Aspect | Backend (Ruff) | Frontend (ESLint + Prettier) |
|--------|----------------|------------------------------|
| **Langage** | Python | TypeScript/React |
| **Vitesse** | ⚡ Ultra-rapide (Rust) | Rapide (Node.js) |
| **Formatage** | ✅ Intégré | ✅ Prettier |
| **Linting** | ✅ Intégré | ✅ ESLint |
| **Import sort** | ✅ Intégré | ❌ Séparé |
| **Config** | 1 fichier | 2 fichiers |
| **Auto-fix** | ✅ Oui | ✅ Oui |

## Avantages

### Ruff
- ✅ Très rapide (10-100x plus rapide que Black/Flake8)
- ✅ Tout-en-un (pas besoin de plusieurs outils)
- ✅ Compatible avec les règles Flake8
- ✅ Mise à jour fréquente

### ESLint + Prettier
- ✅ Standard de l'industrie JavaScript/TypeScript
- ✅ Large écosystème de plugins
- ✅ Prettier : formatage consistant
- ✅ ESLint : détection de bugs

## Ressources

- [Ruff Documentation](https://docs.astral.sh/ruff/)
- [ESLint Rules](https://eslint.org/docs/rules/)
- [Prettier Options](https://prettier.io/docs/en/options.html)
- [React-app ESLint config](https://www.npmjs.com/package/eslint-config-react-app)
