from dev.Day13 import day13

def test_example1():
    depart, buses = """939
7,13,x,x,59,x,31,19""".splitlines()
    depart = int(depart)
    buses = buses.split(",")

    bus_id, minute = day13.get_id_bus_and_remaining_minutes(depart, buses)
    assert 295 == bus_id * minute
test_example1()