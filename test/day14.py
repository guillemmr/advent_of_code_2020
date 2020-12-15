from dev.Day14 import day14

def test_example1():

    init_program = """
mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X
mem[8] = 11
mem[7] = 101
mem[8] = 0""".splitlines()
    memory = day14.init(init_program)
    assert 165 == day14.get_size(memory)
test_example1()