from cffi import FFI
from pathlib import Path

ffi = FFI()

ffi.cdef('''
    void Hello();
''')

path = Path(__file__).parent / 'lib' / 'libhello.so'
lib = ffi.dlopen(str(path))


def hello():
    lib.Hello()
