import re

def read_data(input_data):
    graph = {}
    pattern = re.compile(r"(\w{3}) = \((\w{3}), (\w{3})\)")
    instructions, edges = input_data.split("\n\n")
    for row in edges.strip().splitlines():
        match = pattern.search(row)
        start = match.group(1)
        left = match.group(2)
        right = match.group(3)
        graph[start] = left, right
    return list(map(lambda x: 0 if x == 'L' else 1, instructions)), graph


def run(input_data: list[str]):
    instructions, graph = read_data(input_data)
    steps = 0
    current_node = 'AAA'
    while current_node != 'ZZZ':
        instruction = steps % len(instructions)
        current_node = graph[current_node][instructions[instruction]]
        steps += 1
    return steps
    
if __name__ == "__main__":
    print(run(open("src/2023/data/days/08/data", "r").read()))
