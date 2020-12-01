""" See Readme for problem details"""

from itertools import combinations
import os


def product_of_nums_that_sums_2020(numbers: list) -> int:
    for a, b in combinations(numbers, 2):
        if a + b == 2020:
            return a*b
    raise Exception("No solution")


def read_input_and_solve() -> int:
    with open(os.path.join(os.path.dirname(__file__), "input.txt")) as file:
        numbers = [int(x) for x in file.read().splitlines()]

    return product_of_nums_that_sums_2020(numbers)


if __name__ == "__main__":
    print(read_input_and_solve())
