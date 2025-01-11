import networkx as nx

directions = [1, -1, 1j, -1j]


def read_data(input_data):
    elevation_values = {}
    elevation_chars = {}
    graph = nx.DiGraph()
    starts = []

    for y, row in enumerate(input_data.splitlines()):
        for x, char in enumerate(row):
            elevation_chars[complex(x, y)] = char
            if char == "S":
                elevation_values[complex(x, y)] = ord("a")
            elif char == "E":
                end = complex(x, y)
                elevation_values[complex(x, y)] = ord("z")
            else:
                elevation_values[complex(x, y)] = ord(char)

    for pos, elevation in elevation_values.items():
        for direction in directions:
            next_pos = pos + direction
            if elevation == ord("a"):
                starts.append(pos)
            if next_pos in elevation_values:
                if elevation_values[next_pos] - elevation < 2:
                    graph.add_edge(pos, next_pos)
    return graph, starts, end


def run(input_data):
    graph, starts, end = read_data(input_data)
    return min(
        map(
            lambda x: x[1],
            filter(
                lambda x: x[0] in starts,
                nx.single_target_shortest_path_length(graph, end),
            ),
        )
    )


if __name__ == "__main__":
    print(run(open("src/2022/data/days/12/data", "r").read()))
