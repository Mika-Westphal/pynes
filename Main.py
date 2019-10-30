from Memory import Memory
from CPU import CPU
from Stack import Stack
from Register import Register, Flags, FlagRegister

memory = Memory()
register = Register()
flag_register = FlagRegister()
stack = Stack()
cpu = CPU(memory=memory, registers=register, flag_register=flag_register, stack=stack)


