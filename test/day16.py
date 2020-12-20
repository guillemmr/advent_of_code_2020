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
