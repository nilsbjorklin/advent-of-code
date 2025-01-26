from collections import defaultdict, deque


def read_data(input_data):
    connection = defaultdict(list)
    for line in input_data.splitlines():
        a, b = line.strip().split("-")
        connection[a].append(b)
        connection[b].append(a)
    return connection

def run(input_data):
    connections_for_node = read_data(input_data)
    paths = deque()
    paths.append((["start"]))
    result = 0
    while paths:
        path = paths.popleft()
        if path[-1] == 'end':
            result += 1
        else:
            connections = connections_for_node[path[-1]]
            for connection in connections:
                if connection.upper() == connection or connection not in path:
                    paths.append(path + [connection])
    return result

if __name__ == "__main__":
    print(run(open("src/2021/data/days/12/data", "r").read()))
