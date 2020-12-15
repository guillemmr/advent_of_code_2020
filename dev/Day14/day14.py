import os
import re

def apply_mask(mask: str, value: int) -> int:    
    one_mask = int(mask.replace("X", "0"), 2)
    value = value | one_mask
    zero_mask = int(mask.replace("X", "1"), 2)
    value = value & zero_mask
    return value


def get_adress_and_value(command: str) -> set:
    return map(int, re.findall(r'\d+', command))


def init(init_program: list) -> dict:
    memory = {}
    current_mask = []
    for command in init_program:
        if command.startswith("mask"):
            current_mask = command.split("mask = ")[1]
        elif command.startswith("mem"):
            address, value_to_write = get_adress_and_value(command)
            memory[address] = apply_mask(current_mask, value_to_write)
    return memory


def get_size(memory: dict) -> int:
    size = 0
    for key, value in memory.items():
        size += value
    return size

if __name__ == "__main__":
    with open(os.path.join(os.path.dirname(__file__), "input.txt")) as file:
        init_program = file.read().splitlines()
    memory = init(init_program)
    print(get_size(memory))
    