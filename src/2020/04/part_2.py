import re

required = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}


def read_data(input_data):
    passports = [
        [
            attribute.split(":")
            for attribute in section.replace("\n", " ").strip().split(" ")
        ]
        for section in input_data.split("\n\n")
    ]
    return [{name: value for name, value in fields} for fields in passports]


def run(input_data):
    passports = read_data(input_data)
    valid_passports = list(filter(valid_passport, passports))
    return len(valid_passports)


def valid_passport(passport):
    if not required.issubset(set(passport.keys())):
        return False
    for name, value in passport.items():
        if not valid(name, value):
            return False
    return True


def valid(name, value):
    match name:
        case "byr":
            return valid_range(1920, 2002, value)
        case "iyr":
            return valid_range(2010, 2020, value)
        case "eyr":
            return valid_range(2020, 2030, value)
        case "hgt":
            return valid_height(value)
        case "hcl":
            return valid_hair_color(value)
        case "ecl":
            return valid_eye_color(value)
        case "pid":
            return valid_passport_id(value)
        case _:
            return True


def valid_range(min_year, max_year, value):
    return min_year <= int(value) <= max_year


def valid_height(value):
    matches = re.compile(r"(\d+)(in|cm)").findall(value)
    if not matches:
        return False
    value, unit = matches[0]
    if unit == "in":
        return valid_range(59, 76, value)
    elif unit == "cm":
        return valid_range(150, 193, value)
    return False


def valid_hair_color(value):
    if len(value) != 7:
        return False
    return re.compile(r"#([a-f]|\d){6}").fullmatch(value) is not None


def valid_eye_color(value):
    return value in {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}


def valid_passport_id(value):
    return len(value) == 9 and value.isdigit()


if __name__ == "__main__":
    print(run(open("data", "r").read()))
