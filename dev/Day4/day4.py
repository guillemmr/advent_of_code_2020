from __future__ import annotations
import os


def is_numeric_and_between(value: str, leq: int, geq: int) -> bool:
    try:
        value = int(value)
        if leq <= value and value <= geq:
            return True
    except Exception:
        pass
    return False


def valid_byr(value: str) -> bool:
    return is_numeric_and_between(value, 1920, 2002)


def valid_iyr(value: str) -> bool:
    return is_numeric_and_between(value, 2010, 2020)


def valid_eyr(value: str) -> bool:
    return is_numeric_and_between(value, 2020, 2030)


def valid_hgt(value: str) -> bool:
    try:
        code_type = value[-2:]
        code = value[:-2]
        if "cm" == code_type:
            return is_numeric_and_between(code, 150, 193)
        elif "in" == code_type:
            return is_numeric_and_between(code, 59, 76)
    except Exception:
        pass
    return False


def valid_hcl(value: str) -> bool:
    try:
        if all([len(value) == 7,
                value[:1] == "#",
                value[1:].isalnum()
                ]):
            return True

    except Exception:
        pass
    return False


def valid_ecl(value: str) -> bool:
    return value in ("amb", "blu", "brn", "gry", "grn", "hzl", "oth")


def valid_pid(value: str) -> bool:
    return len(value) == 9 and value.isdigit()


def is_valid_passport(passport: map) -> bool:
    necessary_keys = ("byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid")

    if not all(key in passport for key in necessary_keys):
        return False
    # all necessary keys are in passport

    if all([valid_byr(passport["byr"]),
            valid_iyr(passport["iyr"]),
            valid_eyr(passport["eyr"]),
            valid_hgt(passport["hgt"]),
            valid_hcl(passport["hcl"]),
            valid_ecl(passport["ecl"]),
            valid_pid(passport["pid"])
            ]):
        return True

    return False


def count_valid_passports(passports: list[map]) -> int:
    valid_passports = 0
    for passport in passports:
        if is_valid_passport(passport):
            valid_passports = valid_passports + 1

    return valid_passports


def read_passports(raw_passports: str) -> list[map]:
    passports = []  # <- list of maps
    raw_passports = raw_passports.split("\n\n")
    raw_passports = [passport.replace("\n", " ") for passport in raw_passports]

    for passport in raw_passports:

        passport_map = {}
        keys_vals = passport.split(" ")
        for key_val in keys_vals:

            key, val = key_val.split(":")
            passport_map[key] = val

        passports.append(passport_map)

    return (passports)


if __name__ == "__main__":

    with open(os.path.join(os.path.dirname(__file__), "input.txt")) as file:
        input_passports = file.read()

    passports = read_passports(input_passports)
    print(count_valid_passports(passports))
