directions = {"R": 1, "L": -1, "D": 1j, "U": -1j}


def read_data(input_data):
    moves = []
    for row in input_data.splitlines():
        direction, steps = row.split(" ")
        moves.append((directions[direction], int(steps)))
    return moves


def run(input_data):
    moves = read_data(input_data)
    head = tail = 0j
    tail_visited = set()
    for direction, steps in moves:
        for _ in range(steps):
            head += direction
            diff = head - tail
            x_diff, y_diff = abs(diff.real), abs(diff.imag)
            if x_diff > 1 or y_diff > 1:
                if x_diff > 0:
                    tail += 1 if x_diff == diff.real else -1
                if y_diff > 0:
                    tail += 1j if y_diff == diff.imag else -1j
            tail_visited.add(tail)
    return len(tail_visited)


if __name__ == "__main__":
    print(run(open("src/2022/data/days/09/data", "r").read()))
