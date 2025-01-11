from queue import Queue

pipes = {
    "|": (1j, -1j),
    "-": (1, -1),
    "L": (1, -1j),
    "J": (-1, -1j),
    "7": (-1, 1j),
    "F": (1, 1j),
}

directions = [-1, 1, -1j, 1j]


def read_data(input_data):
    nodes = {
        complex(x, y) if char != "S" else "S": char if char != "S" else complex(x, y)
        for y, line in enumerate(input_data.strip().splitlines())
        for x, char in enumerate(line.strip())
    }

    start = nodes['S']

    queue = Queue()

    for direction in directions:
        next_pos = start + direction
        char = nodes[next_pos]
        if char in pipes:
            for new_direction in pipes[char]:
                if new_direction == direction * -1:
                    queue.put((1, (next_pos)))
    return start, queue, nodes


def run(input_data):
    start, queue, nodes = read_data(input_data)
    distances = {start: 0}

    while not queue.empty():
        distance, pos = queue.get()

        if not pos in distances:
            for direction in pipes[nodes[pos]]:
                queue.put((distance + 1, (pos + direction)))
            distances[pos] = distance
    return max(distances.values())


if __name__ == "__main__":
    print(run(open("src/2023/data/days/10/data", "r").read()))
