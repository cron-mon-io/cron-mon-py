install:
	@uv sync

test: static-tests unit-tests

static-tests:
	@uv run ruff check src tests && uv run ruff format --check src tests && uv run mypy src tests

unit-tests:
	@uv run pytest

format:
	@uv run ruff format src tests
