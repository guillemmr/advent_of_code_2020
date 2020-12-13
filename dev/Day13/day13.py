import os


def get_id_bus_and_remaining_minutes(depart, buses):
    valid_buses = [int(bus) for bus in buses if bus != "x"]
    remaining_minutes = [-((depart % bus)-bus) for bus in valid_buses]
    best_minutes = min(remaining_minutes)
    idx_best_bus = remaining_minutes.index(best_minutes)

    return (valid_buses[idx_best_bus], best_minutes)


def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)


def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m


def solve_congruence(a, b, n) -> set:
    """Returns the pair (A,B) such the sequence {Ax+B}_x_in_Z is the solution of
      ax = b mod (n)"""
    a = a % n
    b = b % n
    a_inverse = modinv(a, n)
    return(n, b*a_inverse % n)


def first_consecutive_depart(buses: list) -> int:
    """ returns a timestamp t such that:
        t = 0 mod buses[0]
        t+1 = 0 mod buses[1]
        ...
        t+n = 0 mod buses[n]
        doesn't include equations where buses[i] is the character "x"
    """
    # The solutions have the form ax+b
    a = 1
    b = 0
    for i, bus in enumerate(buses):
        if bus == "x":
            continue
        bus = int(bus)

        # Solve the equation a*x + b = -i mod bus
        new_a, new_b = solve_congruence(a, -i-b, bus)
        # Ok, x have the form {new_a*n + new_b}_n
        # General sol: a(new_a*n+new_b)+b = (a*new_a)*n +(a*new_b + b) =:a'n+b'
        b = a*new_b + b
        a = a*new_a
    return b % a


if __name__ == "__main__":
    with open(os.path.join(os.path.dirname(__file__), "input.txt")) as file:
        depart, buses = file.read().splitlines()
    depart = int(depart)
    buses = buses.split(",")
    bus_id, minute = get_id_bus_and_remaining_minutes(depart, buses)
    print(bus_id * minute)
    print(first_consecutive_depart(buses))
