directions = [1 + 1j, 1, 1 - 1j, -1 + 1j, -1, -1 - 1j, 1j, -1j]
octopuses = {}


def read_data(input_data):
    global octopuses
    octopuses = {
        complex(x, y): int(char)
        for y, line in enumerate(input_data.splitlines())
        for x, char in enumerate(line)
    }


def run(input_data):
    read_data(input_data)
    step = 1
    while True:
        flashing = increase_octopuses(octopuses.keys())
        has_flashed = set()
        while len(flashing) != 0:
            could_flash = increase_octopuses(neighbors(flashing))
            has_flashed.update(flashing)
            flashing = {pos for pos in could_flash if pos not in has_flashed}
        for octopus in has_flashed:
            octopuses[octopus] = 0
        if len(octopuses) == len(has_flashed):
            return step
        step += 1


def increase_octopuses(positions):
    flashing_octopuses = set()
    for pos in positions:
        octopuses[pos] += 1
        if octopuses[pos] > 9:
            flashing_octopuses.add(pos)
    return flashing_octopuses


def neighbors(positions):
    all_neighbors = []
    for pos in positions:
        for direction in directions:
            if pos + direction in octopuses:
                all_neighbors.append(pos + direction)
    return all_neighbors


if __name__ == "__main__":
    print(run(open("src/2021/data/days/11/data", "r").read()))
