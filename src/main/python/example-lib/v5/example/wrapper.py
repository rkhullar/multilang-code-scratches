from dataclasses import dataclass
from _example import ffi, lib

'''
try:
    from _example import ffi, lib
except ImportError:
    from .build_ffi import builder as ffi
    from .build_ffi import header_path, shared_object_path
    lib = ffi.verify(f'#include "{header_path}"', libraries=[str(shared_object_path)])
'''


@dataclass
class HelloAdapter:

    @staticmethod
    def hello():
        lib.Hello()

    @staticmethod
    def hello_world(name: str):
        # ffi.cast('int', count)
        lib.HelloWorld(ffi.new('char[]', name.encode()))
