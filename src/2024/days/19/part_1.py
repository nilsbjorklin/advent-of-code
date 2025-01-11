def read_data(input_data):
    towel_patterns, design = input_data.split("\n\n")
    return [val.strip() for val in towel_patterns.strip().split(",")], [
        line.strip() for line in design.strip().splitlines()
    ]


def create_towel(towel_patterns, design, index=0):
    if index == len(design):
        return True
    for pattern in towel_patterns:
        if design[index:].startswith(pattern):
            result = create_towel(
                towel_patterns=towel_patterns, design=design, index=index + len(pattern)
            )
            if result:
                return True
    return False


def run(input_data):
    towel_patterns, designs = read_data(input_data)
    result = 0
    for design in designs:
        if create_towel(towel_patterns=towel_patterns, design=design):
            result += 1
    return result


if __name__ == "__main__":
    print(run(open("src/2024/data/days/19/data", "r").read()))
