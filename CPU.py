from Memory import Memory
from FlagRegister import FlagRegister, Flags
from ctypes import c_uint16 as uint16, c_uint8 as uint8

class CPU:
    def __init__(self, mem: Memory):
        self.mem = mem
