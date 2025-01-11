import re


def read_data(input_data):
    pattern = re.compile(r"(\d+),(\d+)")
    return [
        [complex(int(x), complex(y)) for x, y in pattern.findall(row)]
        for row in input_data.splitlines()
    ]


def generate_rocks(formations):
    floor = 0
    rocks = []
    for formation in formations:
        previous_rock = None
        for rock in formation:
            floor = int(max(rock.imag, floor))
            rocks.append(rock)
            if previous_rock is None:
                previous_rock = rock
                continue
            diff = previous_rock - rock
            step = 1 if diff.real > 0 else -1
            if diff.real == 0:
                step = 1j if diff.imag > 0 else -1j
            change = step
            while previous_rock != (rock + step):
                rocks.append(rock + step)
                step += change
            previous_rock = rock
    return floor + 2, rocks


def run(input_data):
    formations = read_data(input_data)
    entry_points = [complex(500, 0)]
    floor, rocks = generate_rocks(formations)
    sand = []

    while len(entry_points) != 0:
        pos = entry_points[-1]
        while pos.imag <= floor:
            next_pos = move_sand(pos, rocks, sand, floor)
            if next_pos == pos:
                if pos == entry_points[-1]:
                    del entry_points[-1]
                sand.append(pos)
                break
            else:
                entry_points.append(next_pos)
                pos = next_pos
    return len(sand)


def move_sand(pos, rocks, sand, floor):
    if floor - pos.imag > 1:
        for direction in [1j, -1 + 1j, 1 + 1j]:
            next_pos = direction + pos
            if next_pos not in rocks and next_pos not in sand:
                return next_pos
    return pos


if __name__ == "__main__":
    print(run(open("src/2022/data/days/14/data", "r").read()))
