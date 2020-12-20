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


def all_values_valids(values: list, expr) -> bool:
    if all(list(map(lambda val: satisfy_rule(expr, val), values))):
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


def discard_invalid_tickets(rules: dict, nearby_tickets: list) -> list:
    valid_tickets = nearby_tickets.copy()
    for ticket in nearby_tickets:
        for value in ticket:
            if not satisfy_some_rule(rules, value):
                valid_tickets.remove(ticket)
    return valid_tickets


def get_unique_field(col: list, fields_to_assign: dict):
    """ Returns the unique field name that satisfies all the values.
        Returns None if more than one field can be assigned.
    """

    unique_field = None

    for field_name, rule in fields_to_assign.items():
        if all_values_valids(col, rule):

            if unique_field is not None:
                return None

            unique_field = field_name

    if unique_field is None:
        raise Exception("Found a column where no field can be assigned!")

    return unique_field


def figure_out_fields(fields: dict, valid_tickets: list) -> dict:
    """ Returns {field_name -> idx of the ticket}.

        Alg: search iteratively for those unasigned ticket idx that a unique
            field can be assigned
    """

    position_fields = {}

    cols_to_assign = list(range(0, len(valid_tickets[0])))
    fields_to_assign = fields.copy()

    while len(cols_to_assign) != 0:

        for col_idx in cols_to_assign:
            col = [ticket[col_idx] for ticket in valid_tickets]

            unique_field = get_unique_field(col, fields_to_assign)

            if unique_field is not None:
                unique_matching_column = col_idx
                break

        if unique_field is None:
            raise Exception("Infinite recursion.")

        cols_to_assign.remove(unique_matching_column)
        fields_to_assign.pop(unique_field)
        position_fields[unique_field] = unique_matching_column

    return position_fields


if __name__ == "__main__":
    with open(os.path.join(os.path.dirname(__file__), "input.txt")) as file:
        raw_rules_and_tickets = file.read()

    info = get_rules_and_tickets(raw_rules_and_tickets)
    rules, my_ticket, nearby_tickets = info

    print(calc_scanning_error_rate(rules, nearby_tickets))

    valid_tickets = discard_invalid_tickets(rules, nearby_tickets)
    position_fields = figure_out_fields(rules, valid_tickets)

    departure_idxs = [idx
                      for field, idx in position_fields.items()
                      if field.startswith("departure")
                      ]

    total_prod = 1
    for idx in departure_idxs:
        total_prod *= my_ticket[idx]
    print(total_prod)
