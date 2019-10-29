from ctypes import c_uint16 as uint16, c_uint8 as uint8

class Memory:
    def __init__(self):
        self.reset()

    def write(self, address: uint16, data: uint8):
        self.mem[address] = data

    def read(self, address: uint16) -> uint8:
        return self.mem[address]

    def dumpMemory(self) -> list:
        return self.mem

    def dumpMemoryToFile(self):
        with open("memory-dump.bin", "wb") as file:
            for i in self.mem:
                file.write(int(i).to_bytes(1, 'little'))

    def reset(self):
        self.mem = [0x00 for x in range(0xFFFF)]