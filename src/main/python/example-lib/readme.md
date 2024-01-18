## Objective
Learn how to create a python library with a go extension. 

### Practical Use Cases
#### JWT
Similar to PyJWT create, decode, sign, and verify tokens using RSA. Implementing the core logic in go should be easier
than c or c++. It should be able to compile for both amd64 and arm64 architectures.

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
