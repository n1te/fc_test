lint:
	ruff check --select I --fix . && ruff format .

test:
	python -m pytest
