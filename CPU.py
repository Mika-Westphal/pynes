from Memory import Memory
from Register import Register, Flags, FlagRegister
from Stack import Stack
from ctypes import c_uint8 as uint8


class CPU:
    def __init__(self, memory: Memory, registers: Register, flag_register: FlagRegister, stack: Stack):
        self.memory = memory
        self.registers = registers
        self.flag_register = flag_register
        self.stack = stack

    def execute_next(self, rom: list):
        cases = {
            "adc": self.adc
        }

    def reset(self):
        self.memory.reset()
        self.registers.reset()
        self.flag_register.reset()
        self.stack.reset()

    def adc(self):
        pass