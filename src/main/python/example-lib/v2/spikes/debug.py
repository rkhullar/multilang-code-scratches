import sys
from pathlib import Path

here = Path(__file__)
# sys.path.insert(-1, str(here.parent))

print(sys.path)

from pyexample import lib, ffi
print(lib.Check)

# import pyexample
# lib, ffi = pyexample.lib, pyexample.ffi
# print(lib.Check)

# from pathlib import Path
# import ctypes



# def load(key: str):
#     path_dir = Path(__file__).parent
#     for path in path_dir.glob(f'{key}.so'):
#         return ctypes.cdll.LoadLibrary(str(path))

'''
# _ = load('libexample')
pyexample = load('pyexample.cpython*')

print(pyexample)
print(pyexample.Check())
# lib, ffi = pyexample.lib, pyexample.ffi
# print(lib.Check)
'''

# from cffi import FFI
# ffi = FFI()
# lib = load('pyexample.cpython*')
# # lib = ffi.dlopen(_lib._name)
#
# print(lib, ffi)
# print(lib.Check)
# print(lib.Check())
# print(lib.Hello(ffi.new('char[]', 'bleh'.encode()), ffi.cast('int', 2)))
