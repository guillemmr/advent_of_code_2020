import os


def count_adj(seats, i, j) -> set:
    occuped = 0

    for di in range(max(i-1, 0), 1+min(i+1, len(seats)-1)):
        for dj in range(max(j-1, 0), 1+min(j+1, len(seats[i])-1)):
            if di == i and dj == j:
                continue

            elif seats[di][dj] == "#":
                occuped += 1

    return occuped


def is_valid(position: list, max_i, max_j):
    if position[0] < 0 or max_i < position[0]:
        return False
    if position[1] < 0 or max_j < position[1]:
        return False
    return True


def count_adj_xrays(seats, i, j) -> set:
    occuped = 0
    directions = [(0, 1), (1, 1), (1, 0), (1, -1),
                  (0, -1), (-1, -1), (-1, 0), (-1, 1)]
    max_i = len(seats)-1
    max_j = len(seats[0])-1
    for dv in directions:
        position = [i+dv[0], j+dv[1]]
        while is_valid(position, max_i, max_j):

            if seats[position[0]][position[1]] == "L":
                break
            if seats[position[0]][position[1]] == "#":
                occuped += 1
                break
            position[0] += dv[0]
            position[1] += dv[1]

    return occuped


def run(seats: list, foo_count_occuped, tolerance) -> list:
    new_seats = seats.copy()
    for i, row in enumerate(seats):
        for j, seat in enumerate(row):
            if seat == ".":
                continue

            occuped = foo_count_occuped(seats, i, j)
            if seat == "L":
                if occuped == 0:
                    """why is so dificult to replace a character?"""
                    new_seats[i] = new_seats[i][:j] + "#" + new_seats[i][j+1:]
            if seat == "#":
                if occuped >= tolerance:
                    """why is so dificult to replace a character?"""
                    new_seats[i] = new_seats[i][:j] + "L" + new_seats[i][j+1:]
    return new_seats


def run_until_stabilize(seats: list, foo_count_occuped, tolerance) -> list:
    new_seats = run(seats, foo_count_occuped, tolerance)
    while seats != new_seats:
        seats = new_seats.copy()
        new_seats = run(seats, foo_count_occuped, tolerance)
    return seats


def count_seats(seats: list) -> int:
    count = 0
    for seats_row in seats:
        for seat in seats_row:
            if seat == "#":
                count += 1
    return count


if __name__ == "__main__":
    with open(os.path.join(os.path.dirname(__file__), "input.txt")) as file:
        raw_seats = file.read().splitlines()
    seats = raw_seats.copy()
    seats = run_until_stabilize(seats, count_adj, tolerance=4)
    print(count_seats(seats))

    seats = raw_seats.copy()
    seats = run_until_stabilize(seats, count_adj_xrays, tolerance=5)
    print(count_seats(seats))
