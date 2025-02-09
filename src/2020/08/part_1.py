import re

accumulator = 0
pointer = 0
visited = set()


def read_data(input_data: str) -> list[tuple[str, int]]:
    pattern = re.compile(r"(\w+) ([+-]\d+)")
    commands = []
    for line in input_data.splitlines():
        command, value = pattern.findall(line)[0]
        commands.append((command, int(value)))
    return commands


def run(input_data: str) -> int:
    commands: list[tuple[str, int]] = read_data(input_data)
    global accumulator, pointer, visited
    while pointer < len(commands):
        if pointer in visited:
            return accumulator
        visited.add(pointer)
        command, value = commands[pointer]
        if command == "acc":
            accumulator += value
        if command == "jmp":
            pointer += value
        else:
            pointer += 1
    return accumulator


if __name__ == "__main__":
    print(run(open("data", "r").read()))
