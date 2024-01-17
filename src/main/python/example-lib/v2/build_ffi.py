from cffi import FFI
from pathlib import Path

name = 'libexample'
path = Path(__file__).parent / 'ext' / 'out'
shared_object_path, header_path = path / f'{name}.so', path / f'{name}.h'

ffi = FFI()

# lib = ffi.dlopen(str(path))

ffi.set_source(module_name='example', source=f'#include "{header_path}"', extra_objects=[str(shared_object_path)])

if __name__ == '__main__':
    ffi.compile(verbose=True, tmpdir='out', target='pyexample.o')
