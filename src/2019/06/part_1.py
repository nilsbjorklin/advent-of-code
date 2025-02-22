from collections import defaultdict

connections = defaultdict(list)
connections_count = defaultdict(int)


def read_data(input_data):
    global connections
    for value in input_data.splitlines():
        center, orbiter = value.split(")")
        connections[center].append(orbiter)


def run(input_data) -> int:
    read_data(input_data)
    check_connections()
    return sum(connections_count.values())


def check_connections(start="COM", depth=0):
    connections_count[start] += depth
    for connected in connections[start]:
        check_connections(connected, depth + 1)


if __name__ == "__main__":
    print(run(open("data").read()))
