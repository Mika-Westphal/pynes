from Memory import Memory
from CPU import CPU
from FlagRegister import *

mem = Memory()
cpu = CPU(mem)
print(mem.read(0x0000))