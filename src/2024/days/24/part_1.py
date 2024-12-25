from collections import defaultdict
import re


gates = defaultdict(bool)
wire_dependencies = defaultdict(set)


def read_data(input_data):
    initial_values, wire_connections = input_data.split("\n\n")
    pattern = re.compile(r"(.{3}) (AND|OR|XOR) (.{3}) -> (.{3})")

    for value in initial_values.strip().splitlines():
        gate, gate_value = value.split(":")
        gates[gate.strip()] = gate_value.strip() == "1"
    wires = [[*match] for match in pattern.findall(wire_connections)]
    for wire in wires:
        first, operation, second, target = wire
        wire_dependencies[first].add((first, operation, second, target))
        wire_dependencies[second].add((first, operation, second, target))
    return wires


def connect_wire(first, operation, second, target):
    if first in gates and second in gates:
        result = None
        if gates[first] and gates[second]:
            result = operation != "XOR"
        elif gates[first] or gates[second]:
            result = operation != "AND"
        else:
            result = 0
        if target not in gates or result != gates[target]:
            gates[target] = result
            if target in wire_dependencies:
                for wires in wire_dependencies[target]:
                    connect_wire(*wires)


def connect_wires(wires):
    for wire in wires:
        connect_wire(*wire)
    return calculate_decimal(), gates


def run(input_data):
    return connect_wires(read_data(input_data)[0])


def calculate_decimal():
    result = 0
    index = 0
    while True:
        key = "z" + str(index).zfill(2)
        if key not in gates:
            return result
        elif gates[key]:
            result += 2**index
        index += 1


if __name__ == "__main__":
    print(run(open("src/2024/data/days/24/data", "r").read()))
