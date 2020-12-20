import os
import line_profiler

profile = line_profiler.LineProfiler()


@profile
def play_one_turn(starting_numbers: list):

    for num in starting_numbers[:-1]:
        yield num

    last_position = {
        val: idx + 1
        for (idx, val) in enumerate(starting_numbers[:-1])
        }

    next_num = starting_numbers[-1]
    current_idx = len(starting_numbers)-1
    del starting_numbers

    while 1:
        current_value = next_num
        current_idx += 1

        try:
            next_num = -last_position[current_value] + current_idx
        except KeyError:
            next_num = 0

        last_position[current_value] = current_idx

        yield current_value


@profile
def play(starting_numbers: list, num_turns: int) -> int:
    """Returns the number that will be played at turn @num_turns"""
    number_played_generator = play_one_turn(starting_numbers)
    for x in range(num_turns-1):
        next(number_played_generator)
    return next(number_played_generator)


if __name__ == "__main__":
    with open(os.path.join(os.path.dirname(__file__), "input.txt")) as file:
        starting_numbers = list(map(int, file.read().split(",")))
    print(play(starting_numbers=starting_numbers, num_turns=2020))
    # num_turns = 30000000
    # print(play(starting_numbers=starting_numbers, num_turns=num_turns))
