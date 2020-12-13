from dev.Day12.day12 import Ship, input_to_movement


def test_1():
    movements = """F10
N3
F7
R90
F11""".splitlines()
    use_waypoint = False
    movements = [input_to_movement(mov, use_waypoint) for mov in movements]
    ship = Ship()
    ship.move(movements)
    assert 25 == ship.taxi_distance()


def test_2():
    movements = """F10
N3
F7
R90
F11""".splitlines()
    use_waypoint = True
    movements = [input_to_movement(mov, use_waypoint) for mov in movements]
    ship = Ship()
    ship.move(movements)
    assert 286 == ship.taxi_distance()
