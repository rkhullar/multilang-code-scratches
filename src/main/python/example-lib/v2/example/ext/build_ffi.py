from cffi import FFI
from pathlib import Path

name = 'libexample'
path = Path(__file__).parent / 'out'
library_path, header_path = path / f'{name}.so', path / f'{name}.h'

builder = FFI()

builder.set_source(
    module_name='pyexample',
    source=f'#include "{header_path}"',
    extra_objects=[str(library_path)]
)

builder.cdef('''
extern void Hello(char* message, int count);
extern void Check();
''')

if __name__ == '__main__':
    builder.compile(verbose=True, tmpdir='out')
