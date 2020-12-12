import os

def turn_ship_clockwise(actual_dir, degrees) -> str:
    if degrees == 90 or degrees == -270:
        if actual_dir == "E": return "S"
        if actual_dir == "S": return "W"
        if actual_dir == "W": return "N"
        if actual_dir == "N": return "E"
    if degrees == 180 or degrees == -180:
        if actual_dir == "E": return "W"
        if actual_dir == "S": return "N"
        if actual_dir == "W": return "E"
        if actual_dir == "N": return "S"
    if degrees == 270 or degrees == -90:
        if actual_dir == "E": return "N"
        if actual_dir == "S": return "E"
        if actual_dir == "W": return "S"
        if actual_dir == "N": return "W"
    raise Exception("ups")


def do_move_ship(ship, actual_dir, type_mov: str, units_mov: int) -> set:
    if type_mov == "N":
        ship["y"] += units_mov
    if type_mov == "S":
        ship["y"] -= units_mov
    if type_mov == "E":
        ship["x"] += units_mov
    if type_mov == "W":
        ship["x"] -= units_mov
    if type_mov == "L":
        actual_dir = turn_ship_clockwise(actual_dir, -units_mov)
    if type_mov == "R":
        actual_dir = turn_ship_clockwise(actual_dir, units_mov)
    if type_mov == "F":
        ship, actual_dir = do_move_ship(ship, actual_dir, actual_dir, units_mov)

    return (ship, actual_dir)


def turn_clockwise_waypoint(position_waypoint, units_mov):
    if units_mov == 90 or units_mov == -270:
        tmp = position_waypoint["y"]
        position_waypoint["y"] = -position_waypoint["x"]
        position_waypoint["x"] = tmp
    if units_mov == 180 or units_mov == -180:
        position_waypoint["y"] = -position_waypoint["y"]
        position_waypoint["x"] = -position_waypoint["x"]
    if units_mov == 270 or units_mov == -90:
        tmp = position_waypoint["y"]
        position_waypoint["y"] = position_waypoint["x"]
        position_waypoint["x"] = -tmp
    return position_waypoint


def do_move_waypoint(ship, waypoint, type_mov: str, units_mov: int) -> set:
    if type_mov == "N":
        waypoint["y"] += units_mov
    if type_mov == "S":
        waypoint["y"] -= units_mov
    if type_mov == "E":
        waypoint["x"] += units_mov
    if type_mov == "W":
        waypoint["x"] -= units_mov
    
    if type_mov == "L":
        waypoint = turn_clockwise_waypoint(waypoint, -units_mov)
    if type_mov == "R":
        waypoint = turn_clockwise_waypoint(waypoint, units_mov)
    if type_mov == "F":
        ship["x"] = ship["x"] + units_mov * waypoint["x"]
        ship["y"] = ship["y"] + units_mov * waypoint["y"]

    return (ship, waypoint)




if __name__ == "__main__":
    with open(os.path.join(os.path.dirname(__file__), "input.txt")) as file:
        movements = file.read()

    movements = movements.splitlines()
    ship = {"x":0, "y":0}
    waypoint = {"x":10, "y":1}
#    actual_dir = "E"

    for mov in movements:
        type_mov = mov[0]
        units_mov = int (mov[1:])
# position, actual_dir = do_move_ship(position, actual_dir,type_mov, units_mov)
        ship, waypoint = do_move_waypoint(ship, waypoint, type_mov, units_mov)
        
    print(ship)
    print(abs(ship["x"])+abs(ship["y"]))

    
