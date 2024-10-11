# Makefile

test:
	pytest-3

build:
	python3 setup.py sdist bdist_wheel

release: clean build
	twine upload dist/*
