import networkx as nx

directions = {"v": 1j, "^": -1j, ">": 1, "<": -1}


def read_data(input_data):
    graph = nx.DiGraph()
    rows = input_data.splitlines()
    end = complex(len(rows[0]) - 2, len(rows) - 1)
    paths = []
    slopes = {}
    for y, row in enumerate(rows):
        for x, char in enumerate(row):
            if char != "#":
                pos = complex(x, y)
                graph.add_node(pos)
                if char == ".":
                    paths.append(pos)
                else:
                    slopes[pos] = directions[char]
    for pos in paths:
        for direction in [1, 1j, -1, -1j]:
            if pos + direction in paths:
                graph.add_edge(pos + direction, pos)
    for pos, slope_direction in slopes.items():
        for direction in [1, 1j, -1, -1j]:
            if direction == slope_direction:
                graph.add_edge(pos, pos + direction)
            elif pos + direction in graph.nodes:
                graph.add_edge(pos + direction, pos)
    return graph, end


def run(input_data):
    graph, end = read_data(input_data)
    return max([len(path) for path in nx.all_simple_paths(graph, 1, end)]) - 1

if __name__ == "__main__":
    print(run(open("src/2023/data/days/23/data", "r").read()))
