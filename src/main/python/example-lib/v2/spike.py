from pathlib import Path
import ctypes
from cffi import FFI


def pick(key: str) -> str:
    path_dir = Path(__file__).parent / 'example' / 'lib'
    for path in path_dir.glob(f'{key}.so'):
        return str(path)
    raise EnvironmentError


x, y = pick('libexample'), pick('pyexample.cpython*')
print(x)
print(y)

ffi = FFI()

lib = ctypes.CDLL(None, ctypes.RTLD_GLOBAL)
ffi.dlopen(str(x))
ffi.dlopen(str(y))

print(lib, ffi)
print(lib.Check)
print(lib.Hello)

print(lib.Check())

lib.Hello.argtypes = [ctypes.c_char_p, ctypes.c_int]
print(lib.Hello.argtypes)


def hello(message: str, count: int):
    lib.Hello(ffi.new('char[]', message.encode()), ffi.cast('int', count))


hello('asdf', 2)


