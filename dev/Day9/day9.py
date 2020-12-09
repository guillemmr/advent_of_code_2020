import os


def is_sum_of_some_pair(sum: int, candidates: list):
    reciprocals = set()
    for i in candidates:
        reciprocals.add(sum - i)
    for i in candidates:
        if i in reciprocals and sum != 2*i:
            return True
    return False


def find_first_xmas_weakness(xmas_code: list, preamble: int):
    """ Returns the first number in @xmas_code, such that:
    1. it's index is > @preamble
    1. Is the first one that is not the sum of two previous @preamble-numbers
    """
    for i, num in enumerate(xmas_code[preamble:]):
        if not is_sum_of_some_pair(num, xmas_code[i: i+preamble]):
            return num


def find_consecutive_sum(total: int, candidates: list):
    min_idx = 0
    max_idx = 0
    partial_sum = 0

    while partial_sum != total:

        if partial_sum < total:
            max_idx = max_idx + 1
        elif partial_sum > total:
            min_idx = min_idx + 1

        partial_sum = sum(candidates[min_idx: max_idx])

    return candidates[min_idx: max_idx]


if __name__ == "__main__":
    with open(os.path.join(os.path.dirname(__file__), "input.txt")) as file:
        xmas_code = file.read()

    xmas_code = [int(x) for x in xmas_code.splitlines()]
    xmas_weakness = find_first_xmas_weakness(xmas_code, 25)
    candidates = find_consecutive_sum(xmas_weakness, xmas_code)
    print(min(candidates)+max(candidates))
