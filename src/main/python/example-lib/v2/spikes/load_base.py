from pathlib import Path
import ctypes
from cffi import FFI


def pick(key: str) -> str:
    path_dir = Path(__file__).parents[1] / 'example' / 'lib'
    for path in path_dir.glob(f'{key}.so'):
        return str(path)
    raise EnvironmentError


x, y = pick('libexample'), pick('pyexample.cpython*')
print(x)
print(y)

ffi = FFI()

lib = ctypes.CDLL(None, ctypes.RTLD_GLOBAL)
ffi.dlopen(str(x))
# ffi.dlopen(str(y))

print(lib, ffi)
print(lib.Check)
print(lib.Hello)

lib.Hello.argtypes = [ctypes.c_char_p, ctypes.c_int]
print(lib.Hello.argtypes)


def check():
    lib.Check()


def hello(message: str, count: int):
    # lib.Hello(ffi.new('char[]', message.encode()), ffi.cast('int', count))
    lib.Hello(message.encode(), count)


if __name__ == '__main__':
    check()
    hello('asdf', 2)

"""
loading the shared object compiled with cffi does nothing in this script
"""