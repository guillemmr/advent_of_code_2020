from dev.Day8 import day8


def test_part1():
    instructions = """nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6"""
    instructions = day8.read_intructions(instructions)
    accumulator, eof = day8.execute_instructions(instructions)
    assert accumulator == 5 and eof is False


def test_part2():
    instructions = """nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6"""
    instructions = day8.read_intructions(instructions)
    instructions = day8.fix(instructions)
    accumulator, eof = day8.execute_instructions(instructions)
    assert accumulator == 8 and eof is True
