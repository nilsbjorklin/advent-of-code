from collections import defaultdict


numbers = {
    0: "abcefd",
    1: "cf",
    2: "acdeg",
    3: "acdfg",
    4: "bcdf",
    5: "abdfg",
    6: "abdefg",
    7: "acf",
    8: "abcdefg",
    9: "abcdfg",
}
numbers_len = {k: len(v) for k, v in numbers.items()}
unique_lens = {2: 1, 4: 4, 3: 7, 7: 8}


def read_data(input_data):
    lines = []
    for line in input_data.splitlines():
        a, b = line.split("|")
        lines.append((a.strip().split(" "), b.strip().split(" ")))
    return lines


def run(input_data: str):
    lines = read_data(input_data)
    result = 0
    for all_values, output in lines:
        value_map = calculate_value_mapping(all_values)
        result += int("".join([value_map["".join(sorted(value))] for value in output]))
    return result


def calculate_value_mapping(all_values):
    known_values = {}
    fives = []
    sixes = []
    for mapping in all_values:
        val_len = len(mapping)
        if val_len in unique_lens:
            known_values[unique_lens[val_len]] = mapping
        elif val_len == 5:
            fives.append(mapping)
        elif val_len == 6:
            sixes.append(mapping)
    char_map = {}
    for real_value in numbers[1]:
        char_map[real_value] = known_values[1]
    for value in known_values[7]:
        if value not in known_values[1]:
            char_map["a"] = value
            break

    for values in sixes:
        missing_number = next(value for value in known_values[8] if value not in values)
        if missing_number in known_values[1]:
            known_values[6] = values
            char_map["c"] = missing_number
            char_map["f"] = next(value for value in char_map["f"] if value not in missing_number)
        else:
            known_values[0 if missing_number in known_values[4] else 9] = values
            
    for values in fives:
        if char_map["c"][0] not in values:
            known_values[5] = values
        else:
            known_values[3 if char_map["f"][0] in values else 2] = values
    return {"".join(sorted(v)): str(k) for k, v in known_values.items()}


if __name__ == "__main__":
    print(run(open("src/2021/data/days/08/data", "r").read()))
