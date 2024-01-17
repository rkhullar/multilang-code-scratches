from cffi import FFI
from pathlib import Path

ffi = FFI()
path = Path(__file__).parent / 'ext' / 'out' / 'libexample.so'
lib = ffi.dlopen(str(path))

if __name__ == '__main__':
    lib.Hello('hello world', 4)
