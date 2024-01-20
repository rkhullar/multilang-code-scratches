try:
    from pyhello import ffi, lib
except ImportError:
    from .build_ffi import builder as ffi
    from .build_ffi import header_code, source_code
    lib = ffi.verify(header_code + source_code)


def hello():
    lib.hello()
