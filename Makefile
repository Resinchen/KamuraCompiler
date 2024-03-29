PYTHON_VERSION := 3.10
VENV ?= .venv

CODE := compiler lrparser


install-poetry:
	curl -sSL https://install.python-poetry.org | python$(PYTHON_VERSION) -

configure-poetry:
	poetry config experimental.new-installer false --local

	poetry config virtualenvs.create true --local
	poetry config virtualenvs.in-project true --local

.create-venv:
	poetry env use python$(PYTHON_VERSION)

init:
	make configure-poetry
	make .create-venv
	poetry install

pretty:
	isort $(CODE) config
	black $(CODE) config
	unify --in-place --recursive $(CODE) config

lint:
	black --check $(CODE)
	flake8 $(CODE) --jobs 4 --statistics
	mypy --install-types --non-interactive $(CODE)

plint: pretty lint