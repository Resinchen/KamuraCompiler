CODE = compiler lrparser

init:
	python -m venv .venv
	source .venv/Scripts/activate
	python -m pip install --upgrade pip
	python -m pip install poetry
	poetry install

lint:
	isort CODE
	black CODE
	flake8 CODE --jobs 4 --statistics