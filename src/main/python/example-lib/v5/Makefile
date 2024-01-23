all: clean build

build:
	python setup.py bdist_wheel
	unzip -l dist/*.whl

clean:
	@rm -rf build dist *.egg-info
	@rm -rf example/local
