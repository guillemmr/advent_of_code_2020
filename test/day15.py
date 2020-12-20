from dev.Day15 import day15


def test_example1():
    assert 436 == day15.play(starting_numbers=[0, 3, 6], num_turns=2020)
    assert 1 == day15.play(starting_numbers=[1, 3, 2], num_turns=2020)
    assert 10 == day15.play(starting_numbers=[2, 1, 3], num_turns=2020)
    assert 27 == day15.play(starting_numbers=[1, 2, 3], num_turns=2020)
    assert 78 == day15.play(starting_numbers=[2, 3, 1], num_turns=2020)
    assert 438 == day15.play(starting_numbers=[3, 2, 1], num_turns=2020)
    assert 1836 == day15.play(starting_numbers=[3, 1, 2], num_turns=2020)
