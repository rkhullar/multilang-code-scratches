from cffi import FFI
from pathlib import Path

ffi = FFI()

ffi.cdef('''
    void Hello();
    void HelloWorld(char* name);
''')
# NOTE: ^ maybe could be loaded from generated header: libhello.h

path = Path(__file__).parent / 'lib' / 'libhello.so'
lib = ffi.dlopen(str(path))


def hello():
    lib.Hello()


def hello_world(name: str):
    lib.HelloWorld(name.encode())
