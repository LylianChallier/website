# Pre-commit Quick Reference

## 🎯 Mode actuel: SOUPLE (non-bloquant)

**Les commits ne sont JAMAIS bloqués** ✅

## Workflow rapide

```bash
# Développement normal
git add .
git commit -m "Message"
# ⚡ Auto-fix + warnings
# ✅ Commit créé quand même
```

## Changer de mode

```bash
./switch-precommit-mode.sh
# 1 = Souple (actuel)
# 2 = Strict (bloque si erreurs)
# 3 = Minimal (formatage seulement)
# 4 = Désactiver
```

## Commandes utiles

```bash
# Tester sans commiter
pre-commit run --all-files

# Bypass ponctuel (urgence)
git commit --no-verify -m "Emergency"

# Désactiver temporairement
pre-commit uninstall
# Réactiver: pre-commit install
```

## Mode actuel détaillé

**Ce qui se passe à chaque commit:**

1. ✅ Ruff lint + format (backend) - Auto-fix
2. ✅ ESLint (frontend) - Auto-fix
3. ✅ Prettier (frontend) - Auto-fix
4. ✅ Checks généraux - Auto-fix

**Comportement:**
- Affiche les corrections
- Montre les warnings
- **Ne bloque JAMAIS**
- Commit toujours créé

## Documentation complète

- [PRE-COMMIT-MODES.md](./PRE-COMMIT-MODES.md) - Tous les modes
- [PRE-COMMIT.md](./PRE-COMMIT.md) - Guide détaillé
- [QUICK-START.md](./QUICK-START.md) - Démarrage rapide
