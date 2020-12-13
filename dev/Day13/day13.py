import os


def get_id_bus_and_remaining_minutes(depart, buses):
    valid_buses = [int(bus) for bus in buses if bus != "x" ]
    remaining_minutes = [-(depart % bus -bus) for bus in valid_buses]
    best_minutes = min(remaining_minutes)
    idx_best_bus = remaining_minutes.index(best_minutes)

    return (valid_buses[idx_best_bus], best_minutes)
    
        

if __name__ == "__main__":
    with open(os.path.join(os.path.dirname(__file__), "input.txt")) as file:
        depart, buses = file.read().splitlines()
    depart = int(depart)
    buses = buses.split(",")
    bus_id, minute = get_id_bus_and_remaining_minutes(depart, buses)
    print(bus_id * minute)

