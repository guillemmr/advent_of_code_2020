from dev.Day6 import day6


def test_part1():
    raw_answers = """abc

a
b
c

ab
ac

a
a
a
a

b"""

    answers = day6.read_answers_by_group(raw_answers)
    assert 11 == day6.sum_answers_by_group(answers, set.union)


def test_part2():
    raw_answers = """abc

a
b
c

ab
ac

a
a
a
a

b"""

    answers = day6.read_answers_by_group(raw_answers)
    assert 6 == day6.sum_answers_by_group(answers, set.intersection)
