import os


def play_one_turn(starting_numbers: list):

    for num in starting_numbers[:-1]:
        yield num

    numbers = starting_numbers.copy()
    last_position = {
        val: idx + 1
        for (idx, val) in enumerate(starting_numbers[:-1])
        }

    while True:
        current_value = numbers[-1]

        if current_value in last_position:
            current_idx = len(numbers)
            next_num = current_idx - last_position[current_value]
        else:
            next_num = 0

        last_position[current_value] = len(numbers)

        numbers.append(next_num)
        yield current_value


def play(starting_numbers: list, num_turns: int) -> int:
    """Returns the number that will be played at turn @num_turns"""
    for turn, value in enumerate(play_one_turn(starting_numbers)):
        if turn == num_turns-1:
            return value


if __name__ == "__main__":
    with open(os.path.join(os.path.dirname(__file__), "input.txt")) as file:
        starting_numbers = list(map(int, file.read().split(",")))

    print(play(starting_numbers=starting_numbers, num_turns=2020))
