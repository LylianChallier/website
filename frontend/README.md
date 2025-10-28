# Frontend React - Portfolio

Application React TypeScript pour le portfolio avec support multilingue.

## Installation

```bash
npm install
```

## Développement

```bash
npm start
# ou
make dev
```

L'application sera accessible sur [http://localhost:3000](http://localhost:3000)

## Build de production

```bash
npm run build
# ou
make build
```

## Linting et formatage

Le projet utilise ESLint et Prettier pour garantir la qualité du code.

### Commandes disponibles

```bash
# Vérifier le code (ESLint)
npm run lint
# ou
make lint

# Formater le code (Prettier)
npm run format
# ou
make format

# Corriger automatiquement les erreurs ESLint
npm run lint:fix

# Vérifier le formatage sans modifier
npm run format:check

# Tout corriger automatiquement
make fix
```

### Configuration

- **ESLint** : [.eslintrc.json](./.eslintrc.json)
- **Prettier** : [.prettierrc.json](./.prettierrc.json)
- **VSCode** : Configuration dans `.vscode/settings.json`

### Extensions VSCode recommandées

Pour une meilleure expérience de développement, installez :
- ESLint (dbaeumer.vscode-eslint)
- Prettier (esbenp.prettier-vscode)

Le formatage automatique à la sauvegarde est déjà configuré.

## Structure

```
src/
├── components/          # Composants React
│   ├── Header.tsx
│   ├── Navigation.tsx
│   ├── Main.tsx
│   └── Footer.tsx
├── api.ts              # API calls
├── i18n.ts             # Configuration i18next
├── types.ts            # Types TypeScript
├── App.tsx             # Composant principal
└── App.css             # Styles globaux
```

## Fonctionnalités

- **React 19** avec TypeScript
- **i18next** pour le support multilingue (FR/EN)
- **Axios** pour les appels API
- **Animations** au scroll et au chargement
- **ESLint + Prettier** pour la qualité du code

## API

Le frontend communique avec le backend Django via :
- `GET /api/portfolio/?lang=fr` - Données en français
- `GET /api/portfolio/?lang=en` - Données en anglais

## Tests

```bash
npm test
# ou
make test
```
