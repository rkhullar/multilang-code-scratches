from pathlib import Path
import ctypes


def pick(key: str) -> str:
    path_dir = Path(__file__).parents[1] / 'example' / 'lib'
    for path in path_dir.glob(f'{key}.so'):
        return str(path)
    raise EnvironmentError


base_path, cffi_path = pick('libexample'), pick('pyexample.cpython*')

ctypes.CDLL(base_path)
pyexample = ctypes.CDLL(cffi_path)
print(pyexample)

print(pyexample.lib)
print(pyexample.ffi)

# print(lib, ffi)
# print(lib.Check)

# lib.Check()
# lib.Hello(ffi.new('char[]', 'asdf'.encode()), ffi.cast('int', 4))

"""
unable to access lib or ffi after loading the library
"""