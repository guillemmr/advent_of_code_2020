from __future__ import annotations
import os


def is_valid_passport(passport: map) -> bool:
    necessary_keys = ("byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid")

    if all(key in passport for key in necessary_keys):
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
