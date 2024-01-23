all: clean build post_build

build:
	python setup.py bdist_wheel
	unzip -l dist/*.whl

clean:
	@rm -rf build dist *.egg-info
	@rm -rf example/local

post_build:
	@rm -rf build *.egg-info
