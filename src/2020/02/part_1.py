def read_data(input_data):
    lines = []
    for row in input_data.splitlines():
        rule, password = row.strip().split(":")
        count, char = rule.split(" ")
        lines.append(((tuple(map(int, count.split("-"))), char), password.strip()))
    return lines


def run(input_data):
    values = read_data(input_data)
    result = 0
    for rule, password in values:
        (min_count, max_count), char = rule
        if min_count <= password.count(char) <= max_count:
            result += 1
    return result


if __name__ == "__main__":
    print(run(open("data", "r").read()))
