from collections import defaultdict, deque
import re


def read_data(input_data):
    starting_input, move_input = input_data.split("\n\n")
    digit = re.compile(r"\d+")

    stack_rows = starting_input.splitlines()
    indexes = []
    stacks = defaultdict(deque)
    for row in stack_rows[::-1]:
        if not indexes:
            indexes = [match.span()[0] for match in digit.finditer(row)]
            continue
        for num, char in enumerate([row[i] for i in indexes]):
            if char.isalpha():
                stacks[num + 1].append(char)

    move_rows = move_input.splitlines()
    moves = [
        (start, dest)
        for repeat, start, dest in [map(int, digit.findall(row)) for row in move_rows]
        for _ in range(repeat)
    ]
    return stacks, moves


def run(input_data):
    stacks, moves = read_data(input_data)
    for start, dest in moves:
        stacks[dest].append(stacks[start].pop())
    return "".join([stack.pop() for stack in stacks.values()])


if __name__ == "__main__":
    print(run(open("src/2022/data/days/05/data", "r").read()))
