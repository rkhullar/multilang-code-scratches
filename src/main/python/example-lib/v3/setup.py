from setuptools import setup, find_packages
# from setuptools.command.build_ext import build_ext


'''
class CustomBuildExt(build_ext):
    def build_extensions(self):
        # go build -buildmode=c-shared -o libhello.so hello.go
        self.run(['go', 'build', '-buildmode=c-shared', '-o', 'example/libhello.so', 'example/hello.go'])
        build_ext.build_extensions(self)
        print('built ext')
'''


setup(
    name='example-lib',
    version='0.1.0',
    packages=find_packages(),
    package_data={'example.lib': ['*.so']},
    include_package_data=True,
    # cffi_modules=['example/build_ffi.py:ffi'],
    install_requires=['cffi'],
    # ext_modules=[],
    # cmdclass={'build_ext': CustomBuildExt}
)
