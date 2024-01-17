# lib = ffi.dlopen(str(path))

# def hello(message: str, count: int):
#     lib.Hello(ffi.new('char[]'), message.encode(), ffi.new('int', count))


from example import lib, ffi

print(lib)