from cffi import FFI
from pathlib import Path

path = Path(__file__).parent.absolute()
header_path = path / 'hello.h'
source_path = path / 'hello.c'

builder = FFI()

builder.set_source(
    module_name='pyhello',
    source=f'#include "{header_path}"',
    sources=[str(source_path)]
)

builder.cdef('''
    void hello();
''')

if __name__ == '__main__':
    builder.compile(verbose=True, tmpdir='out')
