import networkx as nx


graph = nx.Graph()


def read_data(input_data):
    for row in input_data.strip().splitlines():
        graph.add_edge(*(row.strip().split("-")))


def run(input_data):
    read_data(input_data)
    return ",".join(sorted(max(nx.find_cliques(graph), key=len)))


if __name__ == "__main__":
    print(run(open("src/2024/data/days/23/data", "r").read()))
