from dev.Day9 import day9


def test_part1():
    xmas_code = """35
20
15
25
47
40
62
55
65
95
102
117
150
182
127
219
299
277
309
576"""
    xmas_code = [int(x) for x in xmas_code.splitlines()]
    assert 127 == day9.find_first_xmas_weakness(xmas_code, preamble=5)
