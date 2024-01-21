from cffi import FFI
from pathlib import Path

builder = FFI()

path = Path(__file__).parent / 'local'
header_path = path / 'libexample.h'
shared_object_path = path / 'libexample.so'

builder.set_source(
    module_name='_example',
    source=f'#include "{header_path}"',
    libraries=[str(shared_object_path)]
)

builder.cdef('''
    void Hello();
    void HelloWorld(char* name);
''')


if __name__ == '__main__':
    builder.compile(verbose=True)  # tmpdir='out'
