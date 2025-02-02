directions = [1, -1, 1j, -1j]
import networkx as nx

def read_data(input_data):
    lines = input_data.splitlines()
    grid_values = {}
    width = height = len(lines)
    for y, line in enumerate(lines):
        width = len(line)
        for x, char in enumerate(line):
            grid_values[complex(x, y)] = int(char)
    graph = nx.DiGraph()
    for pos, value in grid_values.items():
        for direction in directions:
            if pos + direction in grid_values:
                graph.add_edge(pos + direction, pos, weight=value)
    return graph, width, height
                


def run(input_data):
    graph, width, height = read_data(input_data)
    return nx.shortest_path_length(graph, complex(0,0),complex(width-1, height-1), weight="weight")


if __name__ == "__main__":
    print(run(open("src/2021/data/days/15/data", "r").read()))
