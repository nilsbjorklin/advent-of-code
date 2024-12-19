import networkx as nx

graph = nx.Graph()
directions = [(1, 0), (0, 1)]


def read_data(input_data: str, num_of_bytes):
    return [tuple(map(int, row.strip().split(','))) for row in input_data.strip().splitlines()[:num_of_bytes]]


def build_graph(corrupted_squares, limit):
    for x in range(limit):
        for y in range(limit):
            if (x, y) not in corrupted_squares:
                for x_change, y_change in directions:
                    next_x = x + x_change
                    next_y = y + y_change
                    if 0 > next_x or next_x >= limit or 0 > next_y or next_y >= limit:
                        continue
                    if (next_x, next_y) not in corrupted_squares:
                        graph.add_edge((x, y), (next_x, next_y))


def run(input_data, num_of_bytes, size):
    corrupted_squares = read_data(input_data, num_of_bytes)
    build_graph(corrupted_squares, size)
    return nx.shortest_path_length(graph, (0, 0), (size - 1, size - 1))


if __name__ == '__main__':
    print(run(open('src/2024/data/days/18/data', 'r').read(), 1024, 71))
