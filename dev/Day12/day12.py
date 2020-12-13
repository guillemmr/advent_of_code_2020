import os
import functools
import cmath


class Ship:
    def __init__(self):
        self.position = complex(0)
        self.direction = complex(1)
        self.waypoint = complex(10, 1)

    def move_in_dir(self, n: int):
        self.position += n * self.direction

    def add(self, a):
        self.position += a

    def turn(self, degrees: int):
        """clockwise"""
        a = self.direction
        a *= cmath.exp(-(complex(0, 1)*cmath.pi/180)*degrees)
        self.direction = complex(round(a.real), round(a.imag))

    def move_in_dir_w(self, n: int):
        self.position += n * self.waypoint

    def add_w(self, a):
        self.waypoint += a

    def turn_w(self, degrees: int):
        a = self.waypoint
        a *= cmath.exp(-degrees*cmath.pi/180*complex(0, 1))
        self.waypoint = complex(round(a.real), round(a.imag))

    def move(self, movements: list):
        for mov in movements:
            mov(self)

    def taxi_distance(self):
        return abs(self.position.real) + abs(self.position.imag)


def input_to_movement(str, waypoint):
    type_mov = str[0]
    units_mov = int(str[1:])

    foo_add = Ship.add_w if waypoint is True else Ship.add
    foo_turn = Ship.turn_w if waypoint is True else Ship.turn
    foo_move = Ship.move_in_dir_w if waypoint is True else Ship.move_in_dir

    if type_mov == "N":
        return functools.partial(foo_add, a=complex(0, units_mov))
    if type_mov == "S":
        return functools.partial(foo_add, a=complex(0, -units_mov))
    if type_mov == "E":
        return functools.partial(foo_add, a=complex(units_mov, 0))
    if type_mov == "W":
        return functools.partial(foo_add, a=complex(-units_mov, 0))
    if type_mov == "L":
        degrees = units_mov
        return functools.partial(foo_turn, degrees=-degrees)
    if type_mov == "R":
        degrees = units_mov
        return functools.partial(foo_turn, degrees=degrees)
    if type_mov == "F":
        return functools.partial(foo_move, n=units_mov)


if __name__ == "__main__":
    with open(os.path.join(os.path.dirname(__file__), "input.txt")) as file:
        movements = file.read()

    raw_movs = movements.splitlines()
    use_waypoint = False

    movements = [input_to_movement(mov, use_waypoint) for mov in raw_movs]
    ship = Ship()
    ship.move(movements)
    print(ship.taxi_distance())

    use_waypoint = True
    movements = [input_to_movement(mov, use_waypoint) for mov in raw_movs]
    ship = Ship()
    ship.move(movements)
    print(ship.taxi_distance())
