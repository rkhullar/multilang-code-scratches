# not working
'''
from pathlib import Path
from cffi import FFI

path_dir = Path(__file__).parent / 'ext' / 'out'


def load(key: str):
    _ffi = FFI()
    for path in path_dir.glob(f'{key}.so'):
        _lib = _ffi.dlopen(str(path))
        return _lib, _ffi


base_lib, _ = load('libexample')
lib, ffi = load('example.cpython*')
'''


def x():
    print(1)


from .lib.pyexample import lib, ffi


def check():
    lib.Check()


def hello(message: str, count: int):
    lib.Hello(ffi.new('char[]', message.encode()), ffi.cast('int', count))
