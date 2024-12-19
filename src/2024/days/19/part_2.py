from functools import lru_cache


def read_data(input_data):
    towel_patterns, design = input_data.split("\n\n")
    return [val.strip() for val in towel_patterns.strip().split(",")], [
        line.strip() for line in design.strip().splitlines()
    ]


@lru_cache(None)
def create_towel(towel_patterns, design, index=0):
    result = 0
    if index == len(design):
        return 1
    for pattern in towel_patterns:
        if design[index:].startswith(pattern):
            result += create_towel(
                towel_patterns=tuple(towel_patterns),
                design=design,
                index=index + len(pattern),
            )
    return result


def run(input_data):
    towel_patterns, designs = read_data(input_data)
    result = 0
    for design in designs:
        result += create_towel(towel_patterns=tuple(towel_patterns), design=design)
    return result


if __name__ == "__main__":
    print(run(open("src/2024/data/days/19/data", "r").read()))
