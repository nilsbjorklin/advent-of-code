from functools import reduce
import re

gates = {}
wire_first = []
wire_second = []
wire_operation = []
wire_target = []
operations = {
    "XOR": lambda v1, v2: gates[v1] ^ gates[v2],
    "AND": lambda v1, v2: gates[v1] & gates[v2],
    "OR": lambda v1, v2: gates[v1] | gates[v2],
}


def read_data(input_data):
    global gates, wire_first, wire_operation, wire_second, wire_target
    initial_values, wire_connections = input_data.split("\n\n")
    pattern = re.compile(r"(.{3}) (AND|OR|XOR) (.{3}) -> (.{3})")

    gates = {value.strip()[:3]: False for value in initial_values.strip().splitlines()}

    for wire in [[*match] for match in pattern.findall(wire_connections)]:
        first, operation, second, target = wire
        wire_operation.append(operation)
        wire_first.append(first)
        wire_second.append(second)
        wire_target.append(target)


def test_addition_result():
    last = None
    for i in range(
        reduce(lambda res, x: res + 1 if x.startswith("z") else res, wire_target, 0)
    ):
        z_key = "z" + str(i).zfill(2)
        index = wire_target.index(z_key)
        print(wire_first[index], wire_operation[index], wire_second[index], wire_target[index])

    return [], []


def test_operation_result(operation):
    invalid_outputs = []
    correct_outputs = []
    for i in range(99):
        test_operation(i, operation)
    return invalid_outputs, correct_outputs


def test_operation(i, operation):
    invalid_outputs = []
    correct_outputs = []
    x_key = "x" + str(i).zfill(2)
    y_key = "y" + str(i).zfill(2)
    z_key = "z" + str(i).zfill(2)
    if z_key not in wire_target:
        print(i, z_key)
        return None
    for index in range(len(wire_first)):
        first = wire_first[index]
        second = wire_second[index]
        target = wire_target[index]
        if operation == wire_operation[index]:
            if (first == x_key and second == y_key) or (
                first == y_key and second == x_key
            ):
                if target != z_key:
                    invalid_outputs.append((index, z_key, target))
                else:
                    correct_outputs.append(target)
    if len(invalid_outputs) < i:
        invalid_outputs.append((-1, z_key, None))
    return invalid_outputs, correct_outputs


def run(input_data):
    read_data(input_data)
    swapped = []
    invalid_outputs = correct_outputs = []
    index = 0
    # while True:
    invalid_outputs, correct_outputs = test_addition_result()
    print(invalid_outputs, correct_outputs)
    if not invalid_outputs:
        return ",".join(sorted(swapped))
    swapped += swap(*invalid_outputs[index])
    index += 1


def run_for_and(input_data):
    read_data(input_data)
    swapped = []
    invalid_outputs = correct_outputs = []
    index = 0
    while True:
        invalid_outputs, correct_outputs = test_operation_result("AND")
        print(invalid_outputs, correct_outputs)
        if not invalid_outputs:
            return ",".join(sorted(swapped))
        swapped += swap(*invalid_outputs[index])
        index += 1


def swap(index_index, first, second):
    second_index = wire_target.index(first)
    print(index_index, second_index)
    print(wire_target[index_index], wire_target[second_index])
    wire_target[index_index] = first
    wire_target[second_index] = second
    print(wire_target[index_index], wire_target[second_index])
    return [first, second]


if __name__ == "__main__":
    print(run(open("src/2024/data/days/24/data", "r").read()))
