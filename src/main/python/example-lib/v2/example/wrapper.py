import sys
from pathlib import Path
import os
sys.path.insert(0, str(Path(__file__).parent / 'lib'))
print(sys.path)
print('ld')
print(os.environ.get('LD_LIBRARY_PATH'))

from pyexample import lib, ffi


def x():
    print(1)


def check():
    lib.Check()


def hello(message: str, count: int):
    lib.Hello(ffi.new('char[]', message.encode()), ffi.cast('int', count))
