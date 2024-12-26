from collections import defaultdict
import networkx as nx

graph = None
directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
width = height = 0
start = end = 0


def read_data(input_data: str):
    data = input_data.strip().splitlines()
    global width, height, start, end
    width = len(data[0])
    height = len(data)

    global graph
    graph = nx.grid_2d_graph(width, height)
    walls = []
    for y, row in enumerate(data):
        for x, cell in enumerate(row):
            if cell == "S":
                start = (x, y)
            elif cell == "E":
                end = (x, y)
            elif cell == "#":
                walls.append((x, y))
    for edge in graph.edges:
        if edge[0] in walls or edge[1] in walls:
            graph.remove_edge(*edge)


def run(input_data, threshold=0):
    read_data(input_data)
    shortest_path = nx.shortest_path(graph, start, end)
    result = 0
    for index in range(len(shortest_path)):
        for cheat_end in cheats(shortest_path, index):
            if shortest_path.index(cheat_end) - index - 2 >= threshold:
                result += 1
    return result


def cheats(path, index, cheat=None):
    global tried_cheats
    cur = cheat if cheat else path[index]
    cheat_paths = []
    for new_direction in directions:
        next_step = (new_direction[0] + cur[0], new_direction[1] + cur[1])
        if cheat is not None:
            if next_step in path and path.index(next_step) > index + 2:
                cheat_paths.append(next_step)
        elif next_step not in path:
            cheat_paths += [
                upcoming_step for upcoming_step in cheats(path, index, next_step)
            ]
    return cheat_paths


if __name__ == "__main__":
    print(run(open("src/2024/data/days/20/data", "r").read(), threshold=100))
