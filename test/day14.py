from dev.Day14 import day14


def test_example1():

    init_program = """mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X
mem[8] = 11
mem[7] = 101
mem[8] = 0""".splitlines()

    memory = day14.init(init_program, version_mask=1)
    assert 165 == day14.get_size(memory)


def test_example2():

    init_program = """mask = 000000000000000000000000000000X1001X
mem[42] = 100
mask = 00000000000000000000000000000000X0XX
mem[26] = 1""".splitlines()

    memory = day14.init(init_program, version_mask=2)
    assert 208 == day14.get_size(memory)
