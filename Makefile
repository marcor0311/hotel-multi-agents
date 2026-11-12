.PHONY: install run lint typecheck test
install:
	uv sync --project apps/concierge-api --extra dev
run:
	uv run --project apps/concierge-api uvicorn concierge.main:app --reload --app-dir apps/concierge-api/src
lint:
	uv run --project apps/concierge-api ruff check apps/concierge-api/src apps/concierge-api/tests
typecheck:
	uv run --project apps/concierge-api mypy apps/concierge-api/src
test:
	uv run --project apps/concierge-api pytest apps/concierge-api/tests
