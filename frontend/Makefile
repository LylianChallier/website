.PHONY: help install dev build lint format check fix test

help:
	@echo "Commandes disponibles:"
	@echo "  make install    - Installer les dépendances"
	@echo "  make dev        - Lancer le serveur de développement"
	@echo "  make build      - Build de production"
	@echo "  make lint       - Vérifier le code avec ESLint"
	@echo "  make format     - Formater le code avec Prettier"
	@echo "  make check      - Lint + format check (tout vérifier)"
	@echo "  make fix        - Corriger automatiquement les erreurs"
	@echo "  make test       - Lancer les tests"

install:
	npm install

dev:
	npm start

build:
	npm run build

lint:
	npm run lint

format:
	npm run format

check:
	npm run lint
	npm run format:check

fix:
	npm run lint:fix
	npm run format

test:
	npm test
