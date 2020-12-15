from dev.Day13 import day13


def test_example1():
    depart, buses = """939
7,13,x,x,59,x,31,19""".splitlines()
    depart = int(depart)
    buses = buses.split(",")

    bus_id, minute = day13.get_id_bus_and_remaining_minutes(depart, buses)
    assert 295 == bus_id * minute


def test_example2():
    buses = "17,x,13,19".split(",")
    assert 3417 == day13.first_consecutive_depart(buses)
    buses = "67,7,59,61".split(",")
    assert 754018 == day13.first_consecutive_depart(buses)
    buses = "67,x,7,59,61".split(",")
    assert 779210 == day13.first_consecutive_depart(buses)
    buses = "67,7,x,59,61".split(",")
    assert 1261476 == day13.first_consecutive_depart(buses)
    buses = "1789,37,47,1889".split(",")
    assert 1202161486 == day13.first_consecutive_depart(buses)
