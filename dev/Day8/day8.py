import os


def read_intructions(raw_instructions: str) -> list:
    instructions = []

    for raw_instruction in raw_instructions.split("\n"):
        code, value = raw_instruction.split(" ")
        instructions.append((code, int(value)))

    return instructions


def execute_instructions(instructions: list) -> set:
    # Returns (accumulator when the program finish, or before infinite)
    accumulator = 0
    next_instruction = 0

    instruction_history = {}
    while (next_instruction not in instruction_history
            and next_instruction < len(instructions)):

        instruction_history[next_instruction] = "executed"

        code, value = instructions[next_instruction]
        if code == "nop":
            next_instruction = next_instruction + 1

        elif code == "acc":
            next_instruction = next_instruction + 1
            accumulator = accumulator + value

        elif code == "jmp":
            next_instruction = next_instruction + value

    eof = next_instruction == len(instructions)
    return (accumulator, eof)


def does_finish(instructions: list) -> bool:
    _, eof = execute_instructions(instructions)
    return eof


def fix(instructions: list) -> list:
    # returns the list of instructions with one jmp <-> nop interchanged
    # such that the instructions execution reach EOF

    if does_finish(instructions):
        return instructions

    for n, instruction in enumerate(instructions):
        code, value = instruction
        if code == "nop":
            instructions_fix = instructions.copy()
            instructions_fix[n] = ("jmp", value)
            if does_finish(instructions_fix):
                return instructions_fix

        if code == "jmp":
            instructions_fix = instructions.copy()
            instructions_fix[n] = ("nop", value)
            if does_finish(instructions_fix):
                return instructions_fix

    raise Exception('not fixable!')


if __name__ == "__main__":

    with open(os.path.join(os.path.dirname(__file__), "input.txt")) as file:
        raw_instructions = file.read()
    instructions = read_intructions(raw_instructions)
    instructions = fix(instructions)
    accumulator, have_finished = execute_instructions(instructions)
    print(accumulator)
