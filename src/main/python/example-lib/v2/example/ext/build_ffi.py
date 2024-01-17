from cffi import FFI
from pathlib import Path

name = 'libexample'
path = Path(__file__).parent / 'out'
shared_object_path, header_path = path / f'{name}.so', path / f'{name}.h'

ffi = FFI()

ffi.set_source(module_name='pyexample', source=f'#include "{header_path}"', extra_objects=[str(shared_object_path)])
ffi.cdef('''
extern void Hello(char* message, int count);
extern void Check();
''')

if __name__ == '__main__':
    ffi.compile(verbose=True, tmpdir='out')
