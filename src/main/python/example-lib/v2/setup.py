from setuptools import setup, find_packages

setup(
    name='example-lib',
    version='0.1.0',
    packages=find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
    package_data={'example': ['*.so']},
    include_package_data=True
)
