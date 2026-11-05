# Comandos del proyecto. En Windows sin `make`, usa los comandos equivalentes del README.
PY ?= python
export PYTHONPATH := src

.PHONY: help install data validate test notebook all clean

help:
	@echo "make install   instala dependencias (requirements.txt)"
	@echo "make data      regenera data/interim y data/processed desde data/raw"
	@echo "make validate  revisa la integridad del dataset procesado"
	@echo "make test      ejecuta los tests (validaciones + cifras verificadas)"
	@echo "make notebook  ejecuta el notebook de exploración y guarda las figuras"
	@echo "make all       data + validate + test"

install:
	$(PY) -m pip install -r requirements.txt

data:
	$(PY) -m astrohealth.build

validate:
	$(PY) -m astrohealth.validate

test:
	$(PY) -m pytest -q tests

notebook:
	$(PY) -m jupyter nbconvert --to notebook --execute --inplace notebooks/01-exploracion.ipynb

all: data validate test

clean:
	rm -rf reports/figures/*.png .pytest_cache src/astrohealth/__pycache__ tests/__pycache__
