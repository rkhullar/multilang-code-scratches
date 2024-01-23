from setuptools import setup, find_packages
from wheel.bdist_wheel import bdist_wheel as _bdist_wheel
from pathlib import Path
import subprocess
import sys


def precompile():
    path = Path(__file__).parent.absolute() / 'example'
    subprocess.run('Make', cwd=path)


def patch_wheel_darwin():
    print('need to patch _example.abi3.so in wheel file')


class CustomBuildWheel(_bdist_wheel):
    def run(self):
        precompile()
        _bdist_wheel.run(self)
        if sys.platform == 'darwin':
            patch_wheel_darwin()


setup(
    name='example-lib',
    version='0.1.0',
    packages=find_packages(),
    include_package_data=True,
    cffi_modules=['example/build_ffi.py:builder'],
    install_requires=['cffi'],
    cmdclass={'bdist_wheel': CustomBuildWheel}
)
