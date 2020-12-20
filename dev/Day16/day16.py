import os


def satisfy_rule(expresion, x) -> bool:
    for exp in expresion.split(" or "):
        min_value, max_value = list(map(int, exp.split("-")))
        if min_value <= x and x <= max_value:
            return True
    return False


def satisfy_some_rule(rules, x) -> bool:
    for rule_name, expr in rules.items():
        if satisfy_rule(expr, x):
            return True
    return False


def get_rules_and_tickets(raw_rules_and_tickets):
    main_parts = raw_rules_and_tickets.split("\n\n")
    raw_rules, raw_tikets, raw_nearby_tickets = main_parts

    rules = {}
    for raw_rule in raw_rules.splitlines():
        field_name, expresion = raw_rule.split(":")
        rules[field_name] = expresion

    def str_to_int_list(string: str) -> list:
        return list(map(int, string.split(",")))

    my_ticket = str_to_int_list(raw_tikets.splitlines()[1])

    nearby_tickets = raw_nearby_tickets.splitlines()[1:]
    nearby_tickets = [str_to_int_list(ticket) for ticket in nearby_tickets]

    return (rules, my_ticket, nearby_tickets)


def calc_scanning_error_rate(rules: dict, nearby_tickets: list) -> int:
    # ser := scanning_error_rate
    ser = 0

    for ticket in nearby_tickets:
        for value in ticket:
            if not satisfy_some_rule(rules, value):
                ser += value

    return ser


if __name__ == "__main__":
    with open(os.path.join(os.path.dirname(__file__), "input.txt")) as file:
        raw_rules_and_tickets = file.read()

    info = get_rules_and_tickets(raw_rules_and_tickets)
    rules, my_ticket, nearby_tickets = info

    print(calc_scanning_error_rate(rules, nearby_tickets))
