required = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}


def read_data(input_data):
    return [
        {
            attribute.split(":")[0]
            for attribute in section.replace("\n", " ").strip().split(" ")
        }
        for section in input_data.split("\n\n")
    ]


def run(input_data):
    passports = read_data(input_data)
    return len([passport for passport in passports if required.issubset(passport)])


if __name__ == "__main__":
    print(run(open("data", "r").read()))
