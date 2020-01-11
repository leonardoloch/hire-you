.DEFAULT_GOAL := default_target
.PHONY: default_target test clean setup create-venv setup-dev setup-os git-up code-convention test run all

NPROC := `nproc --all`
PYTEST := py.test -n$(NPROC)
PIP := pip install -r

ADMIN_URL := `openssl rand -base64 48`
SECRET_KEY := `bash scripts/generate-secret-key.sh`

PROJECT_NAME := hire-you
PYTHON_VERSION := 3.7.3
VENV_NAME := $(PROJECT_NAME)-$(PYTHON_VERSION)

# Environment setup
.pip:
	pip install pip --upgrade

setup: .pip
	$(PIP) requirements.txt

setup-dev: .pip
	$(PIP) requirements/local.txt

setup-production: .pip
	$(PIP) requirements/production.txt

.clean-build: ## remove build artifacts
	rm -fr build/
	rm -fr dist/
	rm -fr .eggs/
	find . -name '*.egg-info' -exec rm -fr {} +
	find . -name '*.egg' -exec rm -f {} +

.clean-pyc: ## remove Python file artifacts
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

.clean-test: ## remove test and coverage artifacts
	rm -fr .tox/
	rm -f .coverage
	rm -fr htmlcov/
	rm -fr reports/
	rm -fr .pytest_cache/

clean: .clean-build .clean-pyc .clean-test ## remove all build, test, coverage and Python artifacts

.create-venv:
	pyenv install -s $(PYTHON_VERSION)
	pyenv uninstall -f $(VENV_NAME)
	pyenv virtualenv $(PYTHON_VERSION) $(VENV_NAME)
	pyenv local $(VENV_NAME)

create-venv: .create-venv setup-dev

destroy-env:
	pyenv uninstall -f $(VENV_NAME)

# Repository
git-up:
	git pull
	git fetch -p --all

# Database
db-up:
	python manage.py migrate

migrations:
	python manage.py makemigrations $(APP)


migrations-up:
	make migrations APP=users
	make migrations APP=employers
	make migrations APP=employees


collectstatic:
	python manage.py collectstatic --noinput

code-convention:
	flake8
	pycodestyle


# Tests
test:
	$(PYTEST) --cov-report=term-missing  --cov-report=html --cov=.

# Tests
.check-postgres:
	pgrep -x "postgres" > /dev/null || make run-postgres

test-postgres: .check-postgres
	DATABASE_URL=postgres://postgres:docker@localhost:5432/postgres $(PYTEST) --cov-report=term-missing  --cov-report=html --cov=.
	make kill-postgres;


test-gitlab:
	gitlab-runner exec docker "unit test"

run:
	DJANGO_READ_DOT_ENV_FILE=on python manage.py runserver 0.0.0.0:8000

run-postgres:
	docker run --rm --name pg-docker -e POSTGRES_PASSWORD=docker -d -p 5432:5432 -v $(HOME)/docker/volumes/postgres:/var/lib/postgresql/data postgres

kill-postgres:
	docker kill pg-docker

all: create-venv git-up setup-dev default_target

default_target: clean code-convention test-postgres
