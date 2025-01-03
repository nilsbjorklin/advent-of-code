from collections import deque


directions = [1j, -1j, 1, -1]

ends = set()
visited = set()

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
    while len(positions) != 0:
        step, pos = positions.popleft()
        if step > max_steps:
            break
        print(step, pos, end="")
        if step % 2 == 0:
            ends.add(pos)
        if pos not in visited:
            visited.add(pos)
            for first in directions:
                first_pos = pos + first
                if first_pos in plots and first_pos not in visited:
                    if (step + 1, first_pos) not in positions:
                        positions.append((step + 1, first_pos))
    print_grid(start, ends, plots)
    return len(ends)
def print_grid(start, ends, plots):
    for y in range(140):
        for x in range(140):
            pos = complex(x, y)
            if pos not in plots:
                print('#', end="")
            elif pos in ends:  
                print('O', end="") 
            else:
                print('.', end="") 
        print()


if __name__ == "__main__":
    print(run(open("src/2023/data/days/21/data", "r").read(), 64))
