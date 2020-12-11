from dev.Day10 import day10


def test_example1():
    adapters = """16
10
15
5
1
11
7
19
6
12
4"""
    adapters = day10.get_adapters(adapters)
    adapters_diff = day10.get_full_stack_diff(adapters)
    assert 35 == adapters_diff.count(1)*adapters_diff.count(3)


def test_example2():
    adapters = """16
10
15
5
1
11
7
19
6
12
4"""
    adapters = day10.get_adapters(adapters)
    assert 8 == day10.count_different_stacks(adapters)
