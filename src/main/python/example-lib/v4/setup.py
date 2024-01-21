from setuptools import setup, find_packages

setup(
    name='example-lib',
    version='0.1.0',
    packages=find_packages(),
    include_package_data=True,
    cffi_modules=['example/build_ffi.py:builder'],
    install_requires=['cffi']
)
