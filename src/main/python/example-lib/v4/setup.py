from setuptools import setup, find_packages

setup(
    name='example-lib',
    version='0.1.0',
    packages=find_packages(),
    cffi_modules=['example/build_ffi.py:builder']
)
