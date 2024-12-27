from collections import defaultdict
import networkx as nx
import itertools

path_no_cheat = []

def read_data(input_data):
    data = input_data.strip().splitlines()
    global path_no_cheat
    
    open_squares = set()
    graph = nx.Graph()
    
    for y, row in enumerate(data):
        for x, cell in enumerate(row):
            if cell != "#":
                pos = complex(x, y)
                if cell == "S":
                    start = pos
                elif cell == "E":
                    end = pos
                open_squares.add(pos)
                for direction in [-1, -1j]:
                    prev_pos = pos + direction
                    if prev_pos in open_squares:
                        graph.add_edge(pos, prev_pos)
    
    path_no_cheat = nx.shortest_path(graph, start, end)

def run(input_data, skip_len, threshold):
    read_data(input_data)
    skips = 0    
    grid = defaultdict(list)
    
    for index, pos in enumerate(path_no_cheat):
        grid[(int(pos.real) // skip_len + 1, int(pos.imag) // skip_len + 1)].append((index, pos))
    
    for first_index in range(threshold, len(path_no_cheat)):
        first = path_no_cheat[first_index]
        first_x = int(first.real) // skip_len + 1
        first_y = int(first.imag) // skip_len + 1
        
        for dx, dy in itertools.product([-1, 0, 1], repeat=2):
            neighbor_pos = (first_x + dx, first_y + dy)
            if neighbor_pos in grid:
                for second_index, second in grid[neighbor_pos]:
                    if second_index < first_index - threshold:
                        distance = first - second
                        distance = abs(distance.real) + abs(distance.imag)
                        if distance <= skip_len:
                            if first_index - second_index - distance >= threshold:
                                skips += 1
    return skips

if __name__ == "__main__":
    print(run(open("src/2024/data/days/20/data", "r").read(), skip_len=20, threshold=100))
