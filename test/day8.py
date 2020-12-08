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
    assert 5 == day8.get_accumulator_before_infinite_loop(instructions)