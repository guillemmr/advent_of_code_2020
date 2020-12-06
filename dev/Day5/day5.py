import os


def get_seat_row(seat_code: str) -> int:
    binary_number = seat_code[:7].replace("F", "0").replace("B", "1")
    return int(binary_number, 2)


def get_seat_column(seat_code: str) -> int:
    binary_number = seat_code[7:].replace("L", "0").replace("R", "1")
    return int(binary_number, 2)


def get_seat_id(seat_code: str) -> int:
    return get_seat_row(seat_code)*8+get_seat_column(seat_code)


if __name__ == "__main__":
    with open(os.path.join(os.path.dirname(__file__), "input.txt")) as file:
        seats_id = file.readlines()

    print(max([get_seat_id(x) for x in seats_id]))
