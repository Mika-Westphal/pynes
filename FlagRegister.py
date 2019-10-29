from enum import Enum

class Flags(Enum):
    FLAG_CARRY = 0
    FLAG_ZERO = 1
    FLAG_INTERRUPT_DISABLED = 2
    FLAG_DECIMAL = 3
    FLAG_B_1 = 4
    FLAG_B_2 = 5
    FLAG_OVERFLOW = 6
    FLAG_NEGATIVE = 7

class FlagRegister:
    def __init__(self):
        self.flagREG = (1 << Flags.FLAG_B_2.value)

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