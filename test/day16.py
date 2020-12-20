from dev.Day16 import day16


def test1():
    tickets_info = """class: 1-3 or 5-7
row: 6-11 or 33-44
seat: 13-40 or 45-50

your ticket:
7,1,14

nearby tickets:
7,3,47
40,4,50
55,2,20
38,6,12"""
    info = day16.get_rules_and_tickets(tickets_info)
    rules, my_ticket, nearby_tickets = info
    assert 71 == day16.calc_scanning_error_rate(rules, nearby_tickets)


def test2():
    tickets_info = """class: 0-1 or 4-19
row: 0-5 or 8-19
seat: 0-13 or 16-19

your ticket:
11,12,13

nearby tickets:
3,9,18
15,1,5
5,14,9
"""
    info = day16.get_rules_and_tickets(tickets_info)
    rules, my_ticket, nearby_tickets = info

    valid_tickets = day16.discard_invalid_tickets(rules, nearby_tickets)
    position_fields = day16.figure_out_fields(rules, valid_tickets)

    total_prod = 1
    for idx, field_name in enumerate(position_fields.keys()):
        total_prod *= my_ticket[idx]

    assert 1716 == total_prod
