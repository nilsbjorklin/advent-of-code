from collections import defaultdict
from importlib import import_module
import re


part_1 = import_module("src.2024.days.24.part_1")

gates = defaultdict(bool)
wire_dependencies = defaultdict(set)
wires = []
result_wires = defaultdict(str)


def read_data(input_data):
    global gates, wire_dependencies, wires
    initial_values, wire_connections = input_data.split("\n\n")
    pattern = re.compile(r"(.{3}) (AND|OR|XOR) (.{3}) -> (.{3})")

    for value in initial_values.strip().splitlines():
        gate, gate_value = value.split(":")
        gates[gate.strip()] = gate_value.strip() == "1"
    for index, wire in enumerate([[*match] for match in pattern.findall(wire_connections)]):
        first, operation, second, target = wire
        result_wires[index] = target
        wires.append((first, operation, second))
    set_wire_dependencies()


def set_wire_dependencies():
    global wire_dependencies, wires
    wire_dependencies = defaultdict(set)
    for index, wire in enumerate(wires):
        first, operation, second = wire
        wire_dependencies[first].add((first, operation, second, result_wires[index]))
        wire_dependencies[second].add((first, operation, second, result_wires[index]))


def test_addition_result():
    part_1.gates = gates
    part_1.wire_dependencies = wire_dependencies
    res, _ = part_1.connect_wires(build_wires_part_1())
    return res == calculate_decimal("x") + calculate_decimal("y")

def build_wires_part_1():
    return [(result_wires[index], *wire) for index, wire in enumerate(wires)]

def test_and_result():
    part_1.gates = gates
    part_1.wire_dependencies = wire_dependencies
    print()
    print(bin(calculate_decimal("x"))[2:])
    print(bin(calculate_decimal("y"))[2:])
    res, _ = part_1.connect_wires(build_wires_part_1())
    expected = calculate_decimal("x") & calculate_decimal("y")
    return res == expected, expected ^ res


def run(input_data):
    read_data(input_data)
    if test_addition_result():
        return ""
    return calculate_decimal("z")


def run_for_and(input_data):
    read_data(input_data)
    invalid_indexes = []
    is_correct, difference = test_and_result()
    if is_correct:
        return ""
    else:
        bin_list = list(bin(difference)[2:][::-1])
        for index, bin_digit in enumerate(bin_list):
            if bin_digit == '1':
                invalid_indexes.append('z' + str(index).zfill(2))
    print(invalid_indexes)
    swap(invalid_indexes[0], invalid_indexes[1])
    return calculate_decimal("z")

def swap(first, second):
    for wire in wires:
        print(wire)
    for wire in wire_dependencies.items():
        print(wire)
    for wire in result_wires.items():
        print(wire)


def calculate_decimal(prefix):
    result = 0
    index = 0
    while True:
        key = prefix + str(index).zfill(2)
        if key not in gates:
            return result
        elif gates[key]:
            result += 2**index
        index += 1


if __name__ == "__main__":
    print(run(open("src/2024/data/days/24/data", "r").read()))
