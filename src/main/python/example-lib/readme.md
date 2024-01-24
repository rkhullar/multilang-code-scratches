## Objective
Learn how to create a python library with a go extension.

### Practical Use Cases
#### JWT
Similar to PyJWT create, decode, sign, and verify tokens using RSA. Implementing the core logic in go should be easier
than c or c++. It should be able to compile for both amd64 and arm64 architectures.

### Tool Versions
- python 3.12.1
- golang 1.21.5

### v1
- [x] define `hello` function in `util.go`
- [x] create wrapper in `export.go` with `cgo`
- [x] compile the go code into a shared object `hello.so`
- [x] load `hello.so` into python with `ctypes`
- [x] define signature for go function in python (not ideal)
- [x] define wrapper python function
- [x] invoke function in `example.py`
- [ ] package into library

### v2
- [x] define core `hello` function in `example.go`
- [x] define simple cgo `Check` function in `wrapper.go`
- [x] define cgo `Hello` function in `wrapper.go`
- [x] compile go code into base library `libexample.so`
- [x] use `cffi` to create python module extension `pyexample.cpython-{version}-{platform}.so`
- [x] trust `from pyexample import lib, ffi`
- [x] define python wrapper functions
- [x] setup basic package structure
- [ ] able to install and test wheel file
  - tried package both `*.so` files in package data
  - could not load the cffi binary dynamically
  - tried defining `cffi_modules` in setup script

#### tools
```shell
pip install wheel
pip install cffi
pip install isort
```
```shell
# testing tbd
pip install build
pip install cibuildwheel
```

### v3
similar to v2 except with only one simple go function
- [x] define cgo `Hello` function in `hello.go`
- [x] compile go code into `libhello.so`
- [x] wrap with `cffi` and dynamically load the base library
- [x] include library in `package_data`
- [x] include source go code in `manifest.in`
- [x] able to build and test wheel file
- [x] add second function that accepts a string param

#### caveats
- wheel file does not have platform or version information
  - `example_lib-0.1.0-py3-none-any.whl`
- install requires `cffi`
  - took around 1 minute to install in `docker-test` for `linux/arm64`
  - less than one second for `linux/amd64`

### v4
c extension without go
- [x] define c interface and function in `hello.h` and `hello.c`
- [x] test core c code with `hello_test.c`
- [x] create script to compile extension: `build_ffi.py`
- [x] implement python layer in `wrapper.py`
- [x] define `cffi_modules` in setuptools
- [x] able to build and test wheel file
- [x] include source c code in distributions
- [x] build and test source distribution
  - does not compile on installation; at least compiles into `__pycache__` on import
- [x] how to test without building?
  - wrap extension import in try catch; call ffi verify on import error
  - https://cffi.readthedocs.io/en/latest/cdef.html
- [x] test build in docker for `linux/arm64` and `linux/amd64`
- [x] test usage in lambda function layer
  - successfully built `package.zip` and tested for both runtime architectures
- [ ] expand logic with function that accepts params and returns value

#### caveats
- post installation `pyhello` is located outside the `example` package
```shell
ls venv/lib/python3.12/site-packages
```
```text
pyhello.abi3.so cffi_backend.cpython-312-darwin.so cffi/ example/
```

### v5
- [x] create core logic in `example.go`
  - [x] passing string and int params
  - [x] returning strings
- [x] leverage `cffi` to build the python extension
- [x] create wrapper functions
  - [x] use dataclass to simplify `__init__.py`
  - [x] wrapper functions are static methods
- [x] able to build and test locally
  - [x] include source in wheel file
  - [x] include `libexample.so` in wheel file
  - [x] automate building `libexample.so` during `python setup.py bdist_wheel`
    - extend the `bdist_wheel` with custom wrapper and `cmdclass` keyword in `setup`
    - use `subprocess` to compile the core go code before the normal build steps
  - [x] avoid having to set `LD_LIBRARY_PATH` on linux after install
    - `build_ffi.py` includes extra args to set the relative path such that `_example.abi3.so` can locate `libexample.so`
    - [x] determine if `extra_compile_args` and `extra_link_args` are needed
      - only `extra_link_args` is needed
    - use `ldd _example.abi3.so` to check dependency
  - [x] avoid having to set `DYLD_LIBRARY_PATH` on macos after install
    - `setup.py` patches the wheel file in order to update the dependency from `_example.abi3.so` to `libexample.so`
    - manually this can be done with `otool` for viewing and `install_name_tool` for updating:
    - `otool -L _example.abi3.so`
    - `install_name_tool -change libexample.so @loader_path/example/lib/libexample.so _example.abi3.so` 
- [x] test install from `sdist`
  - no error during install, but did not compile the extension or cgo shared object
- [x] build wheel files in docker for `linux/arm64` and `linux/amd64`
- [x] build lambda function layer `package.zip` archives
- [x] test usage in lambda function

#### caveats
- post installation `_example` is located outside the `example` package
  - might be possible to move post build, or update `module_name` in `build_ffi.py`
- not sure if `build_ffi.py` should be included in wheel file
  - maybe it would be needed for source distributions
- not sure how to develop the python code without installing
  - would probably require core go logic to be compiled beforehand
  - similar to `v4` would need to catch import error and run `lib = ffi.verify`

### Potential Future Work
- try [gopy](https://github.com/go-python/gopy) or [pybindgen](https://pypi.org/project/PyBindGen)
- try [setuptools-golang](https://pypi.org/project/setuptools-golang)
- try [cibuildwheel](https://cibuildwheel.readthedocs.io) for multiple platforms and architectures
- test on windows
- expand core logic with go library like [jwt](https://github.com/golang-jwt/jwt)

## Links
- https://www.ardanlabs.com/blog/2020/07/extending-python-with-go.html
- https://dev.to/astagi/extending-python-with-go-1deb
- https://github.com/go-python/gopy
- https://pkg.go.dev/cmd/cgo
- https://pypi.org/project/cffi
- https://blog.kchung.co/faster-python-with-go-shared-objects
- https://cffi.readthedocs.io/en/latest/cdef.html
- https://last9.io/blog/using-golang-package-in-python-using-gopy
- https://www.nestorsag.com/blog/writing-c-extensions-for-python-with-cffi
- https://itwenty.me/posts/01-understanding-rpath
