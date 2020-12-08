import os


def read_intructions(raw_instructions: str) -> list:
    instructions = []

    for raw_instruction in raw_instructions.split("\n"):
        code, value = raw_instruction.split(" ")
        instructions.append((code, int(value)))

    return instructions


def get_accumulator_before_infinite_loop(instructions: list):
    accumulator = 0
    next_instruction = 0

    instruction_history = {}    
    while next_instruction not in instruction_history:
        instruction_history[next_instruction] = "executed"

        code, value = instructions[next_instruction]
        if code == "nop":
            next_instruction = next_instruction + 1
        
        elif code == "acc":
            next_instruction = next_instruction + 1
            accumulator = accumulator + value
        
        elif code == "jmp":
            next_instruction = next_instruction + value
    
    return accumulator




if __name__ == "__main__":

    with open(os.path.join(os.path.dirname(__file__), "input.txt")) as file:
        raw_instructions = file.read()
    instructions = read_intructions(raw_instructions)
    print ( get_accumulator_before_infinite_loop(instructions))
    