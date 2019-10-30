from ctypes import c_uint8 as uint8


class Stack:
    def __init__(self):
        self.sp = 0xFF  # sp = StackPointer
        self.reset()

    def push(self, data: uint8):
        self.stack.append(data)
        self.sp -= 1

    def pop(self) -> uint8:
        self.sp += 1
        return uint8(self.stack.pop())

    def dump_stack(self) -> list:
        return [self.stack, self.sp]

    def dump_stack_to_file(self):
        with open("stack-dump.bin", "wb") as file:
            for i in self.stack:
                file.write(int(i).to_bytes(1, "little"))
            file.write(int(self.sp).to_bytes(1, "little"))

    def reset(self):
        self.stack = [0x00 for x in range(0xFF)]