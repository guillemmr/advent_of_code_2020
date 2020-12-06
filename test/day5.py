from dev.Day5 import day5


def test_first_part_1():
    seat_code = "BFFFBBFRRR"
    assert 70 == day5.get_seat_row(seat_code)
    assert 7 == day5.get_seat_column(seat_code)
    assert 567 == day5.get_seat_id(seat_code)


def test_first_part_2():
    seat_code = "FFFBBBFRRR"
    assert 14 == day5.get_seat_row(seat_code)
    assert 7 == day5.get_seat_column(seat_code)
    assert 119 == day5.get_seat_id(seat_code)


def test_first_part_3():
    seat_code = "BBFFBBFRLL"
    assert 102 == day5.get_seat_row(seat_code)
    assert 4 == day5.get_seat_column(seat_code)
    assert 820 == day5.get_seat_id(seat_code)


def test_second_part():
    assert 4 == day5.get_missing_seat([1, 2, 3, 5, 6])


def test_missing_seat_always_returns_the_first_seat():
    assert 4 == day5.get_missing_seat([1, 2, 3, 5, 7])
