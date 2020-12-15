import os
import re


def apply_mask_v1(mask: str, value: int) -> list:
    one_mask = int(mask.replace("X", "0"), 2)
    value = value | one_mask
    zero_mask = int(mask.replace("X", "1"), 2)
    value = value & zero_mask
    return value


def get_all_combinations(mask: str) -> list:
    if mask.find("X") == -1:
        return [mask]

    combinations = []
    for index, char in enumerate(mask):
        if char == "X":
            one_mask = mask[:index] + "1" + mask[index+1:]
            combinations += (get_all_combinations(one_mask))
            zero_mask = mask[:index] + "0" + mask[index+1:]
            combinations += (get_all_combinations(zero_mask))
            break
    return combinations


def apply_mask_v2(mask: str, value: int) -> list:
    # applies 1
    one_mask = int(mask.replace("X", "0"), 2)
    value = value | one_mask

    # applies X
    value = format(value, 'b').zfill(len(mask))
    value_masked = []
    for bymask, byvalue in zip(mask, value):
        if bymask == "X":
            value_masked.append("X")
        else:
            value_masked.append(byvalue)
    values = get_all_combinations("".join(value_masked))
    values = [int(value, 2) for value in values]
    return values


def get_address_and_value(command: str) -> set:
    return map(int, re.findall(r'\d+', command))


def init(init_program: list, version_mask: int) -> dict:
    memory = {}
    current_mask = []
    for command in init_program:
        if command.startswith("mask"):
            current_mask = command.split("mask = ")[1]
        elif command.startswith("mem"):
            address, value_to_write = get_address_and_value(command)
            if version_mask == 1:
                memory[address] = apply_mask_v1(current_mask, value_to_write)
            elif version_mask == 2:
                addresses = apply_mask_v2(current_mask, address)
                for i in addresses:
                    memory[i] = value_to_write
    return memory


def get_size(memory: dict) -> int:
    size = 0
    for address, value in memory.items():
        size += value
    return size


if __name__ == "__main__":
    with open(os.path.join(os.path.dirname(__file__), "input.txt")) as file:
        init_program = file.read().splitlines()
    memory = init(init_program, version_mask=1)
    print(get_size(memory))
    memory = init(init_program, version_mask=2)
    print(get_size(memory))
