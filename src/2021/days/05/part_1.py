from collections import defaultdict


def read_data(input_data):
    lines = []
    for line in input_data.splitlines():
        start, end = line.split("->")
        lines.append((complex(*map(int, start.strip().split(","))), complex(*map(int, end.strip().split(",")))))
    return lines


def run(input_data: str):
    lines = read_data(input_data)
    lines_in_pos = defaultdict(int)
    for start, end in lines:
        increment = calculate_increment(start, end)
        if increment is not None:
            lines_in_pos[start]+=1
            while start - end != 0:
                lines_in_pos[end]+=1
                end += increment
    return len(list(filter(lambda x: x > 1, lines_in_pos.values())))


def calculate_increment(start, end):
    diff = start - end
    if diff.real == 0 or diff.imag == 0:
        if diff.real != 0:
            return 1 if diff.real > 0 else -1
        if diff.imag != 0:
            return  1j if diff.imag > 0 else -1j

if __name__ == "__main__":
    print(run(open("src/2021/data/days/05/data", "r").read()))
