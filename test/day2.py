from dev.Day2 import day2


def test_example():
    raw_pswd = """1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc""".splitlines()

    rules, pswds = day2.parse_rules_and_pswds(raw_pswd)
    assert 2 == day2.count_valid_passwords(rules, pswds)
