def read_data(input_data):
    data = []
    for section in input_data.split("\n\n"):
        rows = []
        for row in section.strip().splitlines():
            rows.append(int(row))
        data.append(sum(rows))
    return data

def run(input_data: list[str]):
    data = read_data(input_data)
    return max(data)


if __name__ == "__main__":
    print(run(open("src/2022/data/days/01/data", "r").read()))
