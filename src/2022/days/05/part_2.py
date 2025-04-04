import re


def read_data(input_data):
    starting_input, move_input = input_data.split("\n\n")
    digit = re.compile(r"\d+")

    stack_rows = starting_input.splitlines()
    indexes = []
    stacks = []
    for row in stack_rows[::-1]:
        if not indexes:
            indexes = [match.span()[0] for match in digit.finditer(row)]
            stacks = [[] for _ in indexes]
            continue
        for num, char in enumerate([row[i] for i in indexes]):
            if char.isalpha():
                stacks[num].append(char)

    move_rows = move_input.splitlines()
    moves = [
        (amount, start - 1, dest - 1)
        for amount, start, dest in [map(int, digit.findall(row)) for row in move_rows]
    ]
    return stacks, moves


def run(input_data):
    stacks, moves = read_data(input_data)
    for amount, start, dest in moves:
        stacks[dest] += stacks[start][-amount:]
        stacks[start] = stacks[start][:-amount]
    return "".join([stack[-1] for stack in stacks])


if __name__ == "__main__":
    print(run(open("src/2022/data/days/05/data", "r").read()))
