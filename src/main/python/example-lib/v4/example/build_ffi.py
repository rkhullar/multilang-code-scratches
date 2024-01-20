from cffi import FFI
from pathlib import Path

builder = FFI()

'''
builder.set_source(
    module_name='pyhello',
    source='#include <hello.h>',
    sources=['hello.c']
)
'''

path = Path(__file__).parent
header_path = path / 'hello.h'
source_path = path / 'hello.c'

'''
builder.set_source(
    module_name='pyhello',
    source=f'#include "{header_path}"',
    sources=[str(source_path)]
)
'''

# builder.cdef('''
#     void hello();
# ''')


def read(path: Path) -> str:
    with path.open('r') as f:
        return f.read()


header_code = read(header_path)
source_code = read(source_path)

builder.set_source(
    module_name='pyhello',
    source=header_code + source_code
)

builder.cdef(header_code)

if __name__ == '__main__':
    builder.compile(verbose=True, tmpdir='out')
