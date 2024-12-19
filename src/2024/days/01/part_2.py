def read_data(input_data):
    result = ([], [])
    for i, line in enumerate(input_data):
        parts = line.strip().split()
        if len(parts) == 2:
            result[0].append(int(parts[0]))
            result[1].append(int(parts[1]))
    return sorted(result[0]), sorted(result[1])


def run(input_data: list[str]):
    list_1, list_2 = read_data(input_data)
    similarity = 0
    idx1 = idx2 = 0
    while idx1 < len(list_1) and idx2 < len(list_1):
        val1 = list_1[idx1]
        val2 = list_2[idx2]
        idx1_count = 0
        idx2_count = 0
        if val1 == val2:
            while idx1 < len(list_1) and list_1[idx1] == val2:
                idx1 += 1
                idx1_count += 1
            while idx2 < len(list_2) and val1 == list_2[idx2]:
                idx2 += 1
                idx2_count += 1
        elif val1 < val2:
            idx1 += 1
        else:
            idx2 += 1
        similarity += val1 * idx1_count * idx2_count
    return similarity


if __name__ == "__main__":
    print(run(open("src/2024/data/days/01/data", "r").readlines()))
