import networkx as nx


graph = nx.Graph()
t_nodes = set()


def read_data(input_data):
    for row in input_data.strip().splitlines():
        node_1, node_2 = row.strip().split("-")
        graph.add_edge(node_1, node_2)
        if node_1.startswith('t'):
            t_nodes.add(node_1)
        if node_2.startswith('t'):
            t_nodes.add(node_2)


def run(input_data):
    read_data(input_data)
    cycles = nx.simple_cycles(graph, 3)
    return sum(map(lambda cycle: 1 if t_nodes & set(cycle) else 0, cycles))


if __name__ == "__main__":
    print(run(open("src/2024/data/days/23/data", "r").read()))
