from collections import defaultdict
from copy import deepcopy
import networkx as nx

graph = None
walls = []
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

    start = end = (0, 0)
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


def run(input_data):
    read_data(input_data)
    print(len(graph.edges))
    print_graph(graph, width, height, start, end)
    shortest_path = nx.shortest_path(graph, start, end)
    for node in shortest_path:
        run_cheat(node)


def run_cheat(start_node, skip=None):
    if skip is None:
        for x_change, y_change in directions:
            result.append(run_cheat(start_node, skip + [(start_node=x_change, y_change)]))
    elif len(skip) == 2:
        new_graph = deepcopy(graph)
        new_graph.add_edge(start_node, next_node)
        print_path(nx.shortest_path(new_graph, start, end), skip)
        return nx.shortest_path_length(new_graph, start, end)
    else:
        result = []
        for x_change, y_change in directions:
            result.append(run_cheat(start_node, skip + [(x_change, y_change)]))
        return nx.shortest_path_length(graph, start, end)


def print_path(path, skip):
    print(skip)
    print(len(path))
    for y in range(width):
        row = ""
        for x in range(height):
            if (x, y) == skip_start:
                row += "1"
            elif (x, y) == skip_end:
                row += "2"
            elif (x, y) == start:
                row += "S"
            elif (x, y) == end:
                row += "E"
            elif (x, y) in path:
                row += "*"
            else:
                row += " "
        print(row)


def print_graph(graph, width, height, start, end):
    print(graph.edges)
    path = nx.shortest_path(graph, start, end)
    for y in range(width):
        row = ""
        for x in range(height):
            if (x, y) == start:
                row += "SS"
            elif (x, y) == end:
                row += "EE"
            elif (x, y) in path:
                row += str(path.index((x, y))).zfill(2)
            elif (x, y) in walls:
                row += "##"
            elif (x, y) in graph.nodes:
                row += ".."
            else:
                row += "??????????????"
        print(row)


if __name__ == "__main__":
    print(run(open("src/2024/data/days/20/data", "r").read()))
