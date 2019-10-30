from ctypes import c_uint8 as uint8
from enum import Enum


class InstructionAddressing(Enum):
    pass


class AddressingMode:
    def resolve(self, instruction: uint8):
        pass
