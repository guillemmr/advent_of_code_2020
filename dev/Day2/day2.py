
import os


def parse_rules_and_pswds(rules_and_pswd: list):
    rules = []
    pswds = []
    for rule_and_pswds in rules_and_pswd:
        raw_rule, pswd = rule_and_pswds.split(": ")
        rule = parse_rule(raw_rule)

        rules.append(rule)
        pswds.append(pswd)

    return (rules, pswds)


def parse_rule(raw_rule: str):
    times, letter = raw_rule.split(" ")
    minim, maxim = times.split("-")
    rule = {}
    rule[letter] = (int(minim), int(maxim))
    return rule


def count_valid_passwords(rules: dict, pswds: list):
    valid_passwords = 0
    for rule, pswd in zip(rules, pswds):
        if is_valid_password(rule, pswd):
            valid_passwords = valid_passwords + 1
    return valid_passwords

def only_one_condition(*args):
    return sum(args) == 1

def is_valid_password(rules: dict, psw: str) -> bool:
    for k, v in rules.items():
        index_1 = v[0]
        index_2 = v[1]
    
        if only_one_condition( psw[index_1 - 1] == k, psw[index_2 - 1] == k):
            return True
    return False


if __name__ == "__main__":

    with open(os.path.join(os.path.dirname(__file__), "input.txt")) as file:
        raw_pswd = file.read().splitlines()

    rules, pswds = parse_rules_and_pswds(raw_pswd)
    print(count_valid_passwords(rules, pswds))
