from dev.Day11 import day11


def test_example1():
    seats = """L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL""".splitlines()
    seats = day11.run_until_stabilize(seats, day11.count_adj, 4)

    assert 37 == day11.count_seats(seats)


def test_example2():
    seats = """L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL""".splitlines()

    seats = day11.run_until_stabilize(seats, day11.count_adj_xrays, 5)

    assert 26 == day11.count_seats(seats)
