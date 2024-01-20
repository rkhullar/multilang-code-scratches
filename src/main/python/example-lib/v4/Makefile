all: clean build

build:
	python setup.py sdist bdist_wheel
	unzip -l dist/*.whl

clean:
	@rm -rf build dist *.egg-info
