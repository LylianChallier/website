# Pre-commit Hooks

Configuration des hooks pre-commit pour automatiser le linting et le formatage.

## Installation

### 1. Installer pre-commit

```bash
# Backend
cd backend
pip install pre-commit

# Ou globalement
pip install pre-commit
```

### 2. Installer les hooks

```bash
cd /path/to/website
pre-commit install
```

Cette commande installe les hooks dans `.git/hooks/pre-commit`.

## Hooks configurés

### Backend (Python)
- **Ruff Lint** : Vérifie et corrige automatiquement le code Python
- **Ruff Format** : Formate le code Python

### Frontend (TypeScript/React)
- **ESLint** : Vérifie et corrige le code TypeScript/React
- **Prettier** : Formate le code (TS, TSX, CSS, JSON)

### Hooks généraux
- **trailing-whitespace** : Supprime les espaces en fin de ligne
- **end-of-file-fixer** : Ajoute une ligne vide en fin de fichier
- **check-yaml** : Vérifie la syntaxe YAML
- **check-json** : Vérifie la syntaxe JSON (sauf .vscode/)
- **check-added-large-files** : Empêche les fichiers > 1MB
- **check-merge-conflict** : Détecte les marqueurs de conflit
- **mixed-line-ending** : Normalise les fins de ligne (LF)

## Utilisation

### Automatique (à chaque commit)

Les hooks s'exécutent automatiquement avant chaque commit :

```bash
git add .
git commit -m "Mon message"
# ⚡ Les hooks pre-commit s'exécutent automatiquement
```

Si un hook échoue :
- Les fichiers sont automatiquement corrigés
- Le commit est annulé
- Vous devez re-stagé les fichiers corrigés et recommiter

**Exemple :**
```bash
$ git commit -m "Add feature"
ruff lint (backend)......................................................Passed
ruff format (backend)....................................................Passed
ESLint (frontend)........................................................Failed
- files were modified by this hook

# ESLint a corrigé des fichiers automatiquement
$ git add .
$ git commit -m "Add feature"
# ✅ Tous les hooks passent, commit créé
```

### Manuel (tester avant commit)

```bash
# Tester tous les hooks sur tous les fichiers
pre-commit run --all-files

# Tester tous les hooks sur les fichiers stagés
pre-commit run

# Tester un hook spécifique
pre-commit run ruff
pre-commit run eslint
pre-commit run prettier
```

### Bypass (déconseillé)

Si vous avez vraiment besoin de bypass les hooks :

```bash
git commit --no-verify -m "Message"
# ⚠️ À éviter, utilisez seulement en cas d'urgence
```

## Configuration

Le fichier [.pre-commit-config.yaml](./.pre-commit-config.yaml) contient toute la configuration.

### Structure

```yaml
repos:
  - repo: https://github.com/astral-sh/ruff-pre-commit
    # Hooks Ruff pour Python

  - repo: local
    # Hooks locaux pour npm (ESLint, Prettier)

  - repo: https://github.com/pre-commit/pre-commit-hooks
    # Hooks généraux (whitespace, line endings, etc.)
```

### Personnalisation

Pour modifier la configuration :

1. Éditer `.pre-commit-config.yaml`
2. Mettre à jour les hooks :
   ```bash
   pre-commit install --install-hooks --overwrite
   ```

## Désinstallation

Pour désactiver les hooks :

```bash
pre-commit uninstall
```

Les fichiers de configuration restent, mais les hooks ne s'exécutent plus.

## Troubleshooting

### Les hooks ne s'exécutent pas

```bash
# Vérifier l'installation
pre-commit --version

# Réinstaller
pre-commit install
```

### Hooks trop lents

```bash
# Nettoyer le cache
pre-commit clean
pre-commit gc
```

### Erreur npm dans les hooks

Vérifier que les dépendances frontend sont installées :
```bash
cd frontend
npm install
```

### Mettre à jour les hooks

```bash
pre-commit autoupdate
```

## Intégration CI/CD

Pour utiliser pre-commit en CI :

```yaml
# .github/workflows/lint.yml
name: Lint
on: [push, pull_request]

jobs:
  pre-commit:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
      - name: Install dependencies
        run: |
          pip install pre-commit
          cd frontend && npm install
      - name: Run pre-commit
        run: pre-commit run --all-files
```

## Avantages

✅ **Automatique** : Plus besoin de penser au formatage
✅ **Cohérent** : Même style pour toute l'équipe
✅ **Rapide** : Seulement les fichiers modifiés
✅ **Bloquant** : Impossible de commiter du code mal formaté
✅ **Multi-langages** : Python + TypeScript en un seul endroit

## Commandes rapides

```bash
# Installation
pre-commit install

# Test manuel
pre-commit run --all-files

# Bypass (urgence)
git commit --no-verify

# Désinstaller
pre-commit uninstall

# Mettre à jour
pre-commit autoupdate
```
