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
    sprite = 1
    for i in range(240):
        if i % 40 == 0:
            print()
        print("#" if abs(i % 40 - sprite) < 2 else " ", end="")
        sprite += operations[i]


if __name__ == "__main__":
    run(open("src/2022/data/days/10/data", "r").read())
