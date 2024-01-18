from setuptools import setup, find_packages
from pathlib import Path

ext_path = Path(__file__).parent / 'example' / 'ext'

setup(
    name='example-lib',
    version='0.1.0',
    packages=find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
    package_data={'example.lib': ['*.so']},
    include_package_data=True,
    cffi_modules=[f'{ext_path}/build_ffi.py:builder']
)
