def read_data(input_data):
    return sorted([tuple(map(int, row.split(","))) for row in input_data.splitlines()])


def run(input_data):
    droplets = read_data(input_data)
    connections = 0
    for index in range(len(droplets)):
        for next_index in range(index + 1, len(droplets)):
            cord_diff = [abs(c1 - c2) for c1, c2 in zip(droplets[index], droplets[next_index])]
            if sum(cord_diff) == 1:
                connections += 2
    return len(droplets) * 6 - connections


if __name__ == "__main__":
    print(run(open("src/2022/data/days/18/data", "r").read()))
