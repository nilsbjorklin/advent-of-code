import networkx as nx


def read_data(input_data):
    graph = nx.Graph()
    for value in input_data.splitlines():
        center, orbiter = value.split(")")
        graph.add_edge(center, orbiter)
    return graph


def run(input_data) -> int:
    graph = read_data(input_data)
    return nx.shortest_path_length(graph, "YOU", "SAN") - 2


if __name__ == "__main__":
    print(run(open("data").read()))
