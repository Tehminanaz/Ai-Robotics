.PHONY: lint format

lint:
	ruff check .
	black --check .
	pylint backend

format:
	black .
