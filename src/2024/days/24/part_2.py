import re

wires = []
outputs = []


def read_data(input_data):
    global wires, outputs
    pattern = re.compile(r"(.{3}) (AND|OR|XOR) (.{3}) -> (.{3})")
    wires = [
        [*match]
        for match in pattern.findall(input_data.split("\n\n")[1]
        )
    ]

    outputs = sorted(
        filter(lambda wire: wire.startswith("z"), map(lambda wire: wire[3], wires))
    )[:-1]


def run(input_data):
    read_data(input_data)
    return ",".join(sorted(map(lambda x: x[3], filter(wire_is_invalid, wires))))


def wire_is_invalid(wire):
    first, operator, second, target = wire
    if operator == "XOR":
        if not any(x.startswith(("x", "y", "z")) for x in [target, first, second]):
            return True
        return check_for_wire(target, lambda x: x == "OR")
    elif target in outputs:
        return True
    elif operator == "AND":
        return not {first, second}.union({"x00", "y00"}) and check_for_wire(target, lambda x: x != "OR")
    return False


def check_for_wire(target, operator_invalid):
    for first, operator, second, _ in wires:
        if target in [first, second]:
            if operator_invalid(operator):
                return True
    return False


if __name__ == "__main__":
    print(run(open("src/2024/data/days/24/data", "r").read()))
