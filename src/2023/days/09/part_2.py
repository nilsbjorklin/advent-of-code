def read_data(input_data):
    rows = []
    for row in input_data.strip().splitlines():
        rows.append(list(map(int, row.split(" "))))
    return rows


def run(input_data: list[str]):
    rows = read_data(input_data)
    return sum([add_zero(find_zero_row(row))[0][0] for row in rows])


def find_zero_row(row):
    current_row = [row[index] - row[index - 1] for index in range(1, len(row))]
    if all(value == 0 for value in current_row):
        return [row, current_row]
    else:
        return [row] + find_zero_row(current_row)


def add_zero(rows):
    for index in range(len(rows) - 1, -1, -1):
        if index == len(rows) - 1:
            rows[index].insert(0, 0)
        else:
            rows[index].insert(0, rows[index][0] - rows[index + 1][0])
    return rows


if __name__ == "__main__":
    print(run(open("src/2023/data/days/09/data", "r").read()))
