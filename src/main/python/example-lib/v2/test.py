def hello(message: str, count: int):
    lib.Hello(ffi.new('char[]'), message.encode(), ffi.new('int', count))