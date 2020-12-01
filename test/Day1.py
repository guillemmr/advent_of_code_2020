import sys
print(sys.path)

from dev.Day1 import Day1
import pytest

def test_Exception():
    with pytest.raises(Exception, match=r".*No solution*"):
        Day1.ProductOfNumsThatAdd2020([1,2,3])

def test_solution_example():
    numbers = [1721, 979, 366, 299, 675, 1456]
    result = Day1.ProductOfNumsThatAdd2020(numbers)
    assert result == 514579

def test_solution1():   
    result = Day1.ReadInputAndSolve()
    assert result == 996075
