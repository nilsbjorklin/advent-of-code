from collections import deque


directions = [1j, -1j, 1, -1]

def read_data(input_data):
    start = 0
    plots= []
    for y, row in enumerate(input_data.splitlines()):
        for x, char in enumerate(row):
            if char != '#':
                plots.append(complex(x, y))
                if char == 'S':
                    start = complex(x, y)
    return start, plots

def run(input_data, max_steps):
    start, plots = read_data(input_data)
    positions = deque([[0, start]])
    ends = set()
    visited = set() 
    while len(positions) != 0:
        step, pos = positions.popleft()
        if step > max_steps:
            break
        if step % 2 == 0:
            ends.add(pos)
        if pos not in visited:
            visited.add(pos)
            for direction in directions:
                next_pos = pos + direction
                if next_pos in plots and next_pos not in visited:
                    positions.append((step + 1, next_pos))
    return len(ends)


if __name__ == "__main__":
    print(run(open("src/2023/data/days/21/data", "r").read(), 64))
