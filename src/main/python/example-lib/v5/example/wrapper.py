from dataclasses import dataclass

from _example import ffi, lib


@dataclass
class HelloAdapter:

    @staticmethod
    def hello():
        lib.Hello()

    @staticmethod
    def hello_world(name: str):
        lib.HelloWorld(ffi.new('char[]', name.encode()))

    @staticmethod
    def hello_world_n_times(message: str, count: int = 1):
        params = ffi.new('char[]', message.encode()), ffi.cast('int', count)
        lib.HelloWorldNTimes(*params)

    @staticmethod
    def reverse(text: str) -> str:
        param = ffi.new('char[]', text.encode())
        result = lib.Reverse(param)
        return ffi.string(result).decode()
