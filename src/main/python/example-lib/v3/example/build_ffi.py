from cffi import FFI

ffi = FFI()

ffi.set_source('example._example', None)

if __name__ == '__main__':
    ffi.compile()

'''
tried using with setuptools after missing set_source error
'''