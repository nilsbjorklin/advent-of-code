def read_data(input_data):
    lines = []
    for row in input_data.splitlines():
        rule, password = row.strip().split(":")
        count, char = rule.split(" ")
        indexes = map(int, count.split("-"))
        lines.append((*[password.strip()[value - 1] for value in indexes], char))
    return lines


def run(input_data):
    values = read_data(input_data)
    result = 0
    for first, second, char in values:
        if (first == char) != (second == char):
            result += 1
    return result


if __name__ == "__main__":
    print(run(open("data", "r").read()))
