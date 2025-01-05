def read_data(input_data):
    operations = []
    for row in input_data.splitlines():
        if row == "noop":
            operations.append(0)
        else:
            operations.append(0)
            operations.append(int(row.split(" ")[1]))
    return operations


def run(input_data):
    operations = read_data(input_data)
    vals = [i * sum(operations[: i - 1]) + i for i in range(20, 221, 40)]    
    return sum(vals)


if __name__ == "__main__":
    print(run(open("src/2022/data/days/10/data", "r").read()))
