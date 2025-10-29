# Pre-commit Modes

Le projet propose 3 modes de pre-commit hooks selon vos préférences.

## 🎨 Modes disponibles

### 1. Mode Souple (Soft) - **ACTUEL** ✅

**Fichier:** `.pre-commit-config.yaml` (actif)

**Comportement:**
- ✅ Auto-fixe les erreurs
- ✅ Affiche des warnings
- ✅ **Ne bloque JAMAIS le commit**
- ✅ Verbose pour voir ce qui se passe

**Idéal pour:**
- Développement rapide
- Prototypes
- Éviter les frustrations
- Garder un feedback sans bloquer

**Exemple:**
```bash
$ git commit -m "Work in progress"
⚡ Ruff format: 2 fichiers formatés
⚡ ESLint: 1 warning
✅ Commit créé quand même
```

### 2. Mode Strict (Bloquant)

**Fichier:** `.pre-commit-config-strict.yaml`

**Comportement:**
- ✅ Auto-fixe les erreurs
- ❌ **Bloque le commit si erreurs**
- ⚠️  Nécessite re-commit après fix

**Idéal pour:**
- Production
- Pull requests importantes
- Garantir 100% de qualité
- Travail en équipe strict

**Exemple:**
```bash
$ git commit -m "Add feature"
❌ ESLint: 1 error
❌ Commit bloqué
$ git add .
$ git commit -m "Add feature"
✅ Tout passe, commit créé
```

### 3. Mode Minimal

**Fichier:** `.pre-commit-config-minimal.yaml`

**Comportement:**
- ✅ Formatage automatique seulement
- ✅ Pas de linting
- ✅ Checks critiques uniquement (merge conflicts, large files)
- ✅ Très rapide

**Idéal pour:**
- Commits très fréquents
- Formatage sans vérifications
- Maximum de vitesse

**Exemple:**
```bash
$ git commit -m "Quick fix"
⚡ Prettier: formaté
⚡ Check merge conflicts
✅ Commit créé (5 secondes)
```

## 🔄 Changer de mode

### Méthode automatique (recommandée)

```bash
./switch-precommit-mode.sh
# Suivre les instructions interactives
```

### Méthode manuelle

**Activer le mode strict:**
```bash
mv .pre-commit-config.yaml .pre-commit-config-soft.yaml
mv .pre-commit-config-strict.yaml .pre-commit-config.yaml
pre-commit install --overwrite
```

**Activer le mode minimal:**
```bash
mv .pre-commit-config.yaml .pre-commit-config-soft.yaml
mv .pre-commit-config-minimal.yaml .pre-commit-config.yaml
pre-commit install --overwrite
```

**Revenir au mode souple:**
```bash
mv .pre-commit-config.yaml .pre-commit-config-strict.yaml  # ou minimal
mv .pre-commit-config-soft.yaml .pre-commit-config.yaml
pre-commit install --overwrite
```

## 🎯 Comparaison

| Aspect | Souple | Strict | Minimal |
|--------|--------|--------|---------|
| **Auto-fix** | ✅ | ✅ | ✅ |
| **Linting** | ✅ Warning | ✅ Bloquant | ❌ |
| **Formatage** | ✅ | ✅ | ✅ |
| **Bloque commit** | ❌ Jamais | ✅ Si erreurs | ❌ Jamais |
| **Vitesse** | Moyenne | Moyenne | Rapide |
| **Checks généraux** | ✅ Tous | ✅ Tous | ⚠️  Critiques |
| **Idéal pour** | Dev quotidien | Production | Commits rapides |

## ⚙️ Configuration actuelle

**Mode actif:** Souple (Soft) ✅

**Vérifier:**
```bash
head -3 .pre-commit-config.yaml
# Regarde le commentaire en haut
```

## 📝 Hooks par mode

### Mode Souple (actuel)
```
✅ Ruff Lint (auto-fix, non-bloquant)
✅ Ruff Format (auto-fix)
✅ ESLint (auto-fix, non-bloquant avec || true)
✅ Prettier (auto-fix, non-bloquant avec || true)
✅ Trailing whitespace
✅ End of file fixer
✅ Check YAML
✅ Check JSON
✅ Check large files
✅ Check merge conflicts
✅ Mixed line endings
```

### Mode Strict
```
✅ Ruff Lint (auto-fix, BLOQUANT si échec)
✅ Ruff Format (BLOQUANT si échec)
✅ ESLint (auto-fix, BLOQUANT si échec)
✅ Prettier (auto-fix, BLOQUANT si échec)
✅ Tous les checks généraux (BLOQUANTS)
```

### Mode Minimal
```
✅ Ruff Format seulement
✅ Prettier seulement
⚠️  Check merge conflicts
⚠️  Check large files
```

## 💡 Recommandations

### Développement quotidien
→ **Mode Souple** (actuel)
- Feedback utile sans frustration
- Auto-fix pratique
- Commits fluides

### Avant un push important
→ **Tester en mode Strict**
```bash
./switch-precommit-mode.sh  # Choisir 2
git commit --amend --no-edit
./switch-precommit-mode.sh  # Revenir à 1
```

### Commits très fréquents (TDD, refactoring)
→ **Mode Minimal**
- Formatage seulement
- Maximum de vitesse
- Vérifications manuelles plus tard

### Avant une PR
→ **Mode Strict + vérification manuelle**
```bash
./switch-precommit-mode.sh  # Mode 2
pre-commit run --all-files
# Tout doit passer !
```

## 🚫 Désactiver complètement

```bash
pre-commit uninstall
# Les hooks ne s'exécutent plus

# Réactiver:
pre-commit install
```

## 🔍 Bypass ponctuel

Quel que soit le mode, bypass pour une urgence:
```bash
git commit --no-verify -m "Emergency hotfix"
# ⚠️  À utiliser avec parcimonie !
```

## ✨ Astuce

**Combiner les modes selon le contexte:**

```bash
# WIP quotidien
Mode Souple → Commits fluides

# Avant grosse feature
Mode Strict → Garantir qualité

# Refactoring intensif
Mode Minimal → Vitesse maximum

# Avant merge main
Mode Strict → Vérification finale
```

## 📚 Plus d'infos

- [PRE-COMMIT.md](./PRE-COMMIT.md) - Guide complet
- [.pre-commit-config.yaml](./.pre-commit-config.yaml) - Config actuelle
- [switch-precommit-mode.sh](./switch-precommit-mode.sh) - Script de changement

---

**Mode actuel: Souple ✅**
**Commits jamais bloqués, auto-fix activé, feedback informatif**
