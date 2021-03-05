import struct
import ctypes
RUNNING_ARCH = 'x86' if (struct.calcsize("P") * 8) == 32 else 'x64'

def load_lib(name, arch = None):
    if arch is None:
        arch = RUNNING_ARCH

    return ctypes.cdll.LoadLibrary(__libname(name, arch))


def __libname(name, arch):
    return name + '_' + arch