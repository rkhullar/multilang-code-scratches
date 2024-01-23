from cffi import FFI
from pathlib import Path
import sys


path = Path(__file__).parent.absolute() / 'lib'
header_path = path / 'libexample.h'
shared_object_path = path / 'libexample.so'


def build_extra_set_source_args() -> dict[str, list[str]]:
    match sys.platform:
        case 'linux':
            set_rpath = ['-Wl,-rpath=$ORIGIN/example/lib']
            return dict(extra_compile_arg=set_rpath, extra_link_args=set_rpath)
        case 'darwin':
            return dict()
        case _:
            return dict()


builder = FFI()

builder.set_source(
    module_name='_example',
    source=f'#include "{header_path}"',
    libraries=['example'],
    library_dirs=[str(shared_object_path.parent)],
    **build_extra_set_source_args()
)

builder.cdef('''
    void Hello();
    void HelloWorld(char* name);
    void HelloWorldNTimes(char* message, int count);
    char* Reverse(char* text);
''')


if __name__ == '__main__':
    builder.compile(verbose=True)  # tmpdir='out'
