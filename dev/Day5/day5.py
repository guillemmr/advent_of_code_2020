import os


def get_seat_row(seat_code: str) -> int:
    binary_number = seat_code[:7].replace("F", "0").replace("B", "1")
    return int(binary_number, 2)


def get_seat_column(seat_code: str) -> int:
    binary_number = seat_code[7:].replace("L", "0").replace("R", "1")
    return int(binary_number, 2)


def get_seat_id(seat_code: str) -> int:
    return get_seat_row(seat_code)*8+get_seat_column(seat_code)


def maximum_seat(seats_id: list):
    return max(seats_id)


def get_missing_seat(seats_id: list) -> int:
    seats_id.sort()
    space_between_seats = [y - x for x, y in zip(seats_id[:-1], seats_id[1:])]

    index_of_missing_seat_neighbour = space_between_seats.index(2)
    neighbour_id = seats_id[index_of_missing_seat_neighbour]

    return neighbour_id + 1


if __name__ == "__main__":
    with open(os.path.join(os.path.dirname(__file__), "input.txt")) as file:
        raw_seats = file.readlines()

    all_seats_id = [get_seat_id(x) for x in raw_seats]
    print(maximum_seat(all_seats_id))
    print(get_missing_seat(all_seats_id))
