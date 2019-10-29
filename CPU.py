from Memory import Memory
from ctypes import c_uint16 as uint16, c_uint8 as uint8
from FlagRegister import *

class CPU:
    def __init__(self, mem: uint8):
        self.mem = mem

mem = Memory()
mem.write(0x0000, ord("H"))
mem.write(0x0001, ord("e"))
mem.write(0x0002, ord("l"))
mem.write(0x0003, ord("l"))
mem.write(0x0004, ord("o"))
#mem.dumpMemoryToFile()

flag = FlagRegister()
print(flag.get(Flags.FLAG_B_2))
flag.clear(Flags.FLAG_B_2)
print(flag.get(Flags.FLAG_B_2))
flag.set(Flags.FLAG_B_2)
print(flag.get(Flags.FLAG_B_2))