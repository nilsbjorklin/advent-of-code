import networkx as nx

directions = [1, -1, 1j, -1j]


def read_data(input_data):
    elevation_values = {}
    graph = nx.DiGraph()
    start = end = 0

    for y, row in enumerate(input_data.splitlines()):
        for x, char in enumerate(row):
            if char == "S":
                start = complex(x, y)
                elevation_values[complex(x, y)] = ord("a")
            elif char == "E":
                end = complex(x, y)
                elevation_values[complex(x, y)] = ord("z")
            else:
                elevation_values[complex(x, y)] = ord(char)

    for pos, elevation in elevation_values.items():
        for direction in directions:
            next_pos = pos + direction
            if next_pos in elevation_values:
                if elevation_values[next_pos] - elevation < 2:
                    graph.add_edge(pos, next_pos)
    return graph, start, end


def run(input_data):
    graph, start, end = read_data(input_data)
    return nx.shortest_path_length(graph, start, end)


if __name__ == "__main__":
    print(run(open("src/2022/data/days/12/data", "r").read()))
