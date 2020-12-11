import os


def get_adapters(file_input: str) -> list:
    """ Returns a sorted list of adapters jolts.
     Attach the 0 adapter.
     Attach the last "buit-in" adapters (assumes all adapters can be stacked).
    """
    adapters = list(map(int, file_input.splitlines()))

    zero_adapter = 0
    adapters.append(zero_adapter)

    adapters.sort()

    my_built_in_adapter = adapters[-1] + 3
    adapters.append(my_built_in_adapter)

    return adapters


def get_full_stack_diff(adapters: list) -> list:
    """return the successive jolts differences of the fully stacked adapters"""
    adapters_diff = [y-x for x, y in zip(adapters[0:-1], adapters[1:])]
    return adapters_diff


def can_be_stacked(adapters_subset, adapter_idx):
    jolts_diff = adapters_subset[-1] - adapters_subset[adapter_idx]
    return jolts_diff <= 3


def memorize_helper(f):
    memorized = {}

    def helper(adapters_set):
        jolts = adapters_set[-1]
        if jolts not in memorized:
            memorized[jolts] = f(adapters_set)
        return memorized[jolts]

    return helper


@memorize_helper
def count_different_stacks(adapters_set: list) -> int:
    if len(adapters_set) == 1:
        return 1

    total_stacks = 0

    if len(adapters_set) >= 2 and can_be_stacked(adapters_set, -2):
        total_stacks += count_different_stacks(adapters_set[:-1])

    if len(adapters_set) >= 3 and can_be_stacked(adapters_set, -3):
        total_stacks += count_different_stacks(adapters_set[:-2])

    if len(adapters_set) >= 4 and can_be_stacked(adapters_set, -4):
        total_stacks += count_different_stacks(adapters_set[:-3])

    return total_stacks


if __name__ == "__main__":
    with open(os.path.join(os.path.dirname(__file__), "input.txt")) as file:
        file_input = file.read()
    adapters = get_adapters(file_input)

    # adapters_diff = get_full_stack_diff(adapters)
    # print(adapters_diff.count(1)*adapters_diff.count(3))

    print(count_different_stacks(adapters))
