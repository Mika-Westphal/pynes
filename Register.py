from enum import Enum
from ctypes import c_uint8 as uint8


class Flags(Enum):
    FLAG_CARRY = 0
    FLAG_ZERO = 1
    FLAG_INTERRUPT_DISABLED = 2
    FLAG_DECIMAL = 3
    FLAG_B_1 = 4
    FLAG_B_2 = 5
    FLAG_OVERFLOW = 6
    FLAG_NEGATIVE = 7


class Register:
    def __init__(self):
        self.reset()

    def set(self, register, data: uint8):
        self.register[register] = data

    def get(self, register):
        return self.register[register]

    def reset(self):
        self.register = {"a": 0x00,
                         "x": 0x00,
                         "y": 0x00}


class FlagRegister:
    def __init__(self):
        self.reset()

    def get(self, bit: Flags):
        return self.flagREG & (1 << bit.value)

    def set(self, bit: Flags):
        if self.get(bit) == 0:
            self.flagREG += (1 << bit.value)

    def clear(self, bit: Flags):
        if self.get(bit) > 0:
            self.flagREG -= (1 << bit.value)

    def dump_flags(self):
        return self.flagREG

    def reset(self):
        self.flagREG = (1 << Flags.FLAG_B_2.value)