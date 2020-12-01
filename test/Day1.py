import pytest
from dev.Day1 import Day1


def test_exception():
    with pytest.raises(Exception, match=r".*No solution*"):
        Day1.product_of_nums_that_sums_2020([1, 2, 3])


def test_solution_example():
    numbers = [1721, 979, 366, 299, 675, 1456]
    result = Day1.product_of_nums_that_sums_2020(numbers)
    assert result == 514579


def test_solution1():
    result = Day1.read_input_and_solve()
    assert result == 996075
