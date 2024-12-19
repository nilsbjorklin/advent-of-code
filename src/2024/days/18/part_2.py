import networkx as nx

graph = nx.Graph()
directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def read_data(input_data: str):
    return [tuple(map(int, row.strip().split(','))) for row in input_data.strip().splitlines()]


def build_graph(corrupted_squares, limit):
    for x in range(limit):
        for y in range(limit):
            if (x, y) not in corrupted_squares:
                for x_change, y_change in directions[:2]:
                    next_x = x + x_change
                    next_y = y + y_change
                    if 0 > next_x or next_x >= limit or 0 > next_y or next_y >= limit:
                        continue
                    if (next_x, next_y) not in corrupted_squares:
                        graph.add_edge((x, y), (next_x, next_y))


def add_node(corrupted_squares, index, limit):
    x, y = corrupted_squares[-index]
    for x_change, y_change in directions:
        next_x = x + x_change
        next_y = y + y_change
        if 0 > next_x or next_x >= limit or 0 > next_y or next_y >= limit:
            continue
        if (next_x, next_y) not in corrupted_squares:
            graph.add_edge((x, y), (next_x, next_y))
        elif corrupted_squares.index((next_x, next_y)) > index:
            graph.add_edge((x, y), (next_x, next_y))
    return x, y


def run(input_data, size):
    corrupted_squares = read_data(input_data)
    build_graph(corrupted_squares, size)
    graph.add_node((size - 1, size - 1))

    for i in range(len(corrupted_squares)):
        add_node(corrupted_squares, i, size)
        if nx.has_path(graph, (0, 0), (size - 1, size - 1)):
            return ','.join(map(str, corrupted_squares[-i]))


if __name__ == '__main__':
    print(run(open('src/2024/data/days/18/data', 'r').read(), 71))
