.PHONY: help lint format check install

help:
	@echo "Commandes disponibles:"
	@echo "  make install    - Installer les dépendances"
	@echo "  make lint       - Vérifier le code avec Ruff"
	@echo "  make format     - Formater le code avec Ruff"
	@echo "  make check      - Lint + format (tout vérifier)"
	@echo "  make fix        - Corriger automatiquement les erreurs"

install:
	pip install -r requirements.txt

lint:
	ruff check .

format:
	ruff format .

check: lint
	ruff format --check .

fix:
	ruff check --fix .
	ruff format .
