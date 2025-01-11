from copy import deepcopy
from math import lcm
import re


def read_data(input_data):
    graph = {}
    pattern = re.compile(r"(\w{3}) = \((\w{3}), (\w{3})\)")
    instructions, edges = input_data.split("\n\n")
    start_nodes = []
    for row in edges.strip().splitlines():
        match = pattern.search(row)
        start = match.group(1)
        if start.endswith("A"):
            start_nodes.append(start)
        left = match.group(2)
        right = match.group(3)
        graph[start] = left, right
    return list(map(lambda x: 0 if x == "L" else 1, instructions)), start_nodes, graph


def run(input_data: list[str]):
    instructions, start_nodes, graph = read_data(input_data)
    cycles = []
    for node in start_nodes:
        cycle = find_cycle(graph, deepcopy(instructions), node)
        cycles.append(cycle)
    return lcm(*cycles)


def find_cycle(graph, instructions, node):
    current_node = node
    steps = 0
    instruction = steps % len(instructions)
    while True:
        if current_node.endswith("Z"):
            return steps
        instruction = steps % len(instructions)
        current_node = graph[current_node][instructions[instruction]]
        steps += 1


if __name__ == "__main__":
    print(run(open("src/2023/data/days/08/data", "r").read()))
