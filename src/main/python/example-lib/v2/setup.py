from setuptools import setup, Extension

setup(
    name='example-lib',
    version='0.1.0',
    packages=['example'],
    ext_modules=[Extension('example', [])]
)
