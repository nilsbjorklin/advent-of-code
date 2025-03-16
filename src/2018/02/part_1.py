def read_data(input_data):
    return [sorted(row.strip()) for row in input_data.splitlines()]


def run(input_data) -> int:
    values = read_data(input_data)
    triplets = doubles = 0
    for value in values:
        [has_double, has_triplet] = doubles_triples_count(value)
        doubles += has_double
        triplets += has_triplet
    return triplets * doubles


def doubles_triples_count(value):
    has_triplet = has_double = 0
    for char in set(value):
        char_count = value.count(char)
        if char_count == 2:
            has_double = 1
        if char_count == 3:
            has_triplet = 1
    return [has_double, has_triplet]


if __name__ == "__main__":
    print(run(open("data", "r").read()))
