from collections import deque
from copy import deepcopy
import re
import networkx as nx

valves = {}
tunnels = {}

def read_data(input_data):
    global valves, tunnels
    pattern = re.compile(r"Valve (\w{2})\D+(\d+).*?valve[s]? (.*)")
    graph = nx.Graph()
    for row in input_data.splitlines():
        valve, flow, ends = pattern.findall(row)[0]
        valves[valve] = int(flow)
        for end in ends.split(", "):
            graph.add_edge(valve, end)
    tunnels = dict(nx.all_pairs_shortest_path_length(graph))


def run(input_data):
    read_data(input_data)
    options = set(filter(lambda x: valves[x] != 0, tunnels))
    best_path_value = 0
    paths = deque([[[], 30, 0]])
    while len(paths) != 0:
        order, time_left, score = deepcopy(paths.popleft())
        if len(order) == 0:
            pos = 'AA'
        else:
            pos = order[-1]
            time_left -= 1
            score += valves[pos]*time_left
            best_path_value = max(best_path_value, score)
        unvisited = options.difference(order)
        if score + sum(map(lambda x: valves[x] * time_left, unvisited)) < best_path_value:
            continue
        if time_left <= 0:
            continue
        if len(unvisited) != 0:
            unvisited_value = {next_pos: valves[next_pos]*(time_left - tunnels[pos][next_pos]) for next_pos in unvisited}
            for next_pos in [k for k, _ in sorted(unvisited_value.items(), key=lambda item: item[1], reverse=True)]:                
                paths.append((order + [next_pos], time_left - tunnels[pos][next_pos], score))
    return best_path_value
        
        
if __name__ == "__main__":
    print(run(open("src/2022/data/days/16/data", "r").read()))
