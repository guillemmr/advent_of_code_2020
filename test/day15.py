from dev.Day15.day15 import play


def test_example1():
    assert 436 == play(starting_numbers=[0, 3, 6], num_turns=2020)
    assert 1 == play(starting_numbers=[1, 3, 2], num_turns=2020)
    assert 10 == play(starting_numbers=[2, 1, 3], num_turns=2020)
    assert 27 == play(starting_numbers=[1, 2, 3], num_turns=2020)
    assert 78 == play(starting_numbers=[2, 3, 1], num_turns=2020)
    assert 438 == play(starting_numbers=[3, 2, 1], num_turns=2020)
    assert 1836 == play(starting_numbers=[3, 1, 2], num_turns=2020)


def un_test_example2():
    num_turns = 30000000
    assert 175594 == play(starting_numbers=[0, 3, 6], num_turns=num_turns)
    assert 2578 == play(starting_numbers=[1, 3, 2], num_turns=num_turns)
    assert 3544142 == play(starting_numbers=[2, 1, 3], num_turns=num_turns)
    assert 261214 == play(starting_numbers=[1, 2, 3], num_turns=num_turns)
    assert 6895259 == play(starting_numbers=[2, 3, 1], num_turns=num_turns)
    assert 18 == play(starting_numbers=[3, 2, 1], num_turns=num_turns)
    assert 362 == play(starting_numbers=[3, 1, 2], num_turns=num_turns)
