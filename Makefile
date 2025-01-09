
reuse:
	uv run pytest -v -s test_fixture_reuse.py

black:
	uv run black -l 130 *.py
	uv run ruff check
