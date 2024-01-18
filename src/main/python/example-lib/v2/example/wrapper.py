from pyexample import lib, ffi


def x():
    print(1)


def check():
    lib.Check()


def hello(message: str, count: int):
    lib.Hello(ffi.new('char[]', message.encode()), ffi.cast('int', count))
