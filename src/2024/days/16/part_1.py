import networkx as nx

turns = [1, -1, 1j, -1j]


def read_data(input_data: str):
    graph = nx.Graph()
    nodes = {
        x + y * 1j: col
        for y, row in enumerate(input_data.strip().splitlines())
        for x, col in enumerate(row.strip())
        if col != "#"
    }
    start = list(nodes.keys())[list(nodes.values()).index("S")]
    end = list(nodes.keys())[list(nodes.values()).index("E")]

    for direction in turns:
        for pos in nodes.keys():
            if pos != start or direction == 1:
                for turn in turns:
                    next_pos = pos + turn
                    if next_pos in nodes:
                        weight = 1 if turn == direction else 1001
                        next_node = (
                            (next_pos, turn) if next_pos != end else (next_pos, 0)
                        )
                        graph.add_edge((pos, direction), next_node, weight=weight)
    return start, end, graph


def run(input_data):
    start, end, graph = read_data(input_data)
    return nx.shortest_path_length(graph, (start, 1), (end, 0), weight="weight")


if __name__ == "__main__":
    print(run(open("src/2024/data/days/16/data", "r").read()))
