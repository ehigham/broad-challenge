.PHONY: clean lint dist test coverage install

help:
	@echo "clean       - remove all build, test, coverage and Python artifacts"
	@echo "lint        - check style with pylint"
	@echo "test        - run tests quickly with the default Python"
	@echo "coverage    - check code coverage quickly with the default Python"
	@echo "dist        - package"
	@echo "install     - install the package to the active Python's site-packages"

clean: clean-build clean-pyc clean-test

clean-build:
	rm -fr build/
	rm -fr dist/
	rm -fr .eggs/
	find . -name '*.egg-info' -exec rm -fr {} +
	find . -name '*.egg' -exec rm -f {} +

clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

clean-test:
	rm -f .coverage

lint:
	python -m pylint --exit-zero challenge test

test:
	python setup.py test

coverage:
	python -m coverage run --source challenge setup.py test
	python -m coverage report -m

dist: clean
	python setup.py sdist
	python setup.py bdist_wheel
	ls -l dist

install: clean
	python setup.py install