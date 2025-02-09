import re


def read_data(input_data: str) -> list[tuple[str, int]]:
    pattern = re.compile(r"(\w+) ([+-]\d+)")
    commands = []
    for line in input_data.splitlines():
        command, value = pattern.findall(line)[0]
        commands.append((command, int(value)))
    return commands


def run(input_data: str) -> int:
    commands: list[tuple[str, int]] = read_data(input_data)
    change_index = 0
    while True:
        while commands[change_index][0] == "acc":
            change_index += 1
        command, value = commands[change_index]
        commands[change_index] = ("jmp" if command == "nop" else "nop", value)
        result = test(commands)
        if result is not None:
            return result
        else:
            command, value = commands[change_index]
            commands[change_index] = ("jmp" if command == "nop" else "nop", value)
            change_index += 1


def test(commands):
    accumulator = 0
    pointer = 0
    visited = set()
    while pointer < len(commands):
        if pointer in visited:
            return None
        visited.add(pointer)
        command, value = commands[pointer]
        if command == "acc":
            accumulator += value
        pointer += value if command == "jmp" else 1
    return accumulator


if __name__ == "__main__":
    print(run(open("data", "r").read()))
