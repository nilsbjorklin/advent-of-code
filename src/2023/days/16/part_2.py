from collections import deque

mirrors = {
    "/": {1j: [-1], 1: [-1j], -1j: [1], -1: [1j]},
    "\\": {1j: [1], 1: [1j], -1j: [-1], -1: [-1j]},
    "-": {1j: [1, -1], 1: [1], -1j: [1, -1], -1: [-1]},
    "|": {1j: [1j], 1: [1j, -1j], -1j: [-1j], -1: [1j, -1j]},
}
mirror_positions = {}
y_len = x_len = None
energized = set()


def read_data(input_data):
    global mirror_positions, y_len, x_len
    rows = input_data.splitlines()
    y_len = len(rows)
    x_len = len(rows[0])
    for y, row in enumerate(rows):
        for x, val in enumerate(row):
            if val in mirrors:
                mirror_positions[complex(x, y)] = val


def run(input_data):
    read_data(input_data)
    global energized
    max_energized = 0
    for index in range(y_len):
        energized = set()
        start_pos = index*1j - 1
        max_energized = max(run_simulation(start_pos, 1), max_energized)
    for index in range(y_len):
        energized = set()
        start_pos = index*1j + x_len
        max_energized = max(run_simulation(start_pos, -1), max_energized)
    for index in range(x_len):
        energized = set()
        start_pos = index - 1j
        max_energized = max(run_simulation(start_pos, 1j), max_energized)
    for index in range(x_len):
        energized = set()
        start_pos = index + y_len*1j
        max_energized = max(run_simulation(start_pos, -1j), max_energized)
    return max_energized

def run_simulation(start_pos, direction):
    beams = deque([(start_pos, direction)])
    while len(beams) != 0:
        beam = beams.popleft()
        for new_beam in simulate_beam(beam):
            beams.append(new_beam)
    return len({pos for pos, _ in energized})

def simulate_beam(beam):
    pos, direction = beam
    next_pos = pos + direction
    while 0 <= next_pos.real < x_len and 0 <= next_pos.imag < y_len:
        if (next_pos, direction) in energized:
            return []
        else:
            energized.add((next_pos, direction))
            if next_pos in mirror_positions:
                return list(
                    map(
                        lambda x: (next_pos, x),
                        mirrors[mirror_positions[next_pos]][direction],
                    )
                )
            else:
                next_pos += direction
    return []

if __name__ == "__main__":
    print(run(open("src/2023/data/days/16/data", "r").read()))
