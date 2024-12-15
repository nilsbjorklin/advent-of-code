def read_data(input_data):
    result = ([], [])
    for (i, line) in enumerate(input_data):
        parts = line.strip().split()
        if len(parts) == 2:
            result[0].append(int(parts[0]))
            result[1].append(int(parts[1]))
    return sorted(result[0]), sorted(result[1])


def run(input_data: list[str]):
    list_1, list_2 = read_data(input_data)
    diff = 0
    for i in range(len(list_1)):
        diff += abs(list_1[i] - list_2[i])
    return diff


if __name__ == '__main__':
    print(run(open('../../data/days/01/data', 'r').readlines()))
