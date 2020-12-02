""" See Readme for problem details"""

from itertools import combinations
import os
import numpy


def product_nums_that_sums_2020(list_numbers: list, group_length: int) -> int:
    """Find those numbers that adds to 2020 and return their product.

    Args:
        list_numbers (list): candidates to find which ones adds 2020
        group_length (int): length of the searching group.
            For example, if = 1, check if there's a single candidate 2020.
                         if = 2,  search two candidates that adds 2020.

    Raises:
        Exception: No solution.

    Returns:
        int: Product of numbers that sums 2020
    """

    for current_candidates in combinations(list_numbers, group_length):
        if numpy.sum(current_candidates) == 2020:
            return numpy.prod(current_candidates)
    raise Exception("No solution")


def read_input_and_solve(group_length: int) -> int:
    with open(os.path.join(os.path.dirname(__file__), "input.txt")) as file:
        numbers = [int(x) for x in file.read().splitlines()]

    return product_nums_that_sums_2020(numbers, group_length)


if __name__ == "__main__":
    print(read_input_and_solve(3))
