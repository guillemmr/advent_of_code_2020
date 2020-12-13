import os


def count_adj(seats, i, j) -> set:
    free = 0
    occuped = 0

    for di in range(max(i-1,0), 1+min(i+1,len(seats)-1)):
        for dj in range(max(j-1,0), 1+min(j+1,len(seats[i])-1)):

            if di == i and dj == j:
                continue

            if seats[di][dj] == "L":
                free += 1
            elif seats[di][dj] == "#":
                occuped += 1

    return (free, occuped)
    

def run(seats:list) -> list:
    new_seats = seats.copy()
    for i, row in enumerate(seats):
        for j, seat in enumerate(row):
            if seat == ".":
                continue
            new_row = new_seats[i]

            free, occuped = count_adj(seats, i, j) 
            if seat == "L":
                if occuped == 0:
                    new_seats[i] = new_seats[i][:j]+ "#" + new_seats[i][j+1:]
            if seat == "#":
                if occuped >= 4:
                    new_seats[i] = new_seats[i][:j]+ "L" + new_seats[i][j+1:]
    return new_seats

def run_until_stabilize(seats:list) -> list:
    new_seats = run(seats)
    while seats != new_seats:
        seats = new_seats.copy()
        new_seats = run(seats)
    return seats


def count_seats(seats:list) -> int:
    count = 0
    for seats_row in seats:
        for seat in seats_row:
            if seat == "#":
                count += 1
    return count

if __name__ == "__main__":
    with open(os.path.join(os.path.dirname(__file__), "input.txt")) as file:
        seats = file.read().splitlines()

    seats = run_until_stabilize(seats)
    print(count_seats(seats))
