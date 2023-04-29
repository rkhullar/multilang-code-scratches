import ctypes
from pathlib import Path

shared_object_path = Path(__file__).parent / 'ext' / 'hello.so'
shared_object = ctypes.cdll.LoadLibrary(str(shared_object_path))

_hello = shared_object.Hello
_hello.argtypes = [ctypes.c_char_p]
_hello.restype = ctypes.c_char_p

_free = shared_object.free
_free.argtypes = [ctypes.c_void_p]


def hello(message: str) -> str:
    result = _hello(message.encode())
    _free(result)
    return result
