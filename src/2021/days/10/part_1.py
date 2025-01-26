chunk_start = {"(", "[", "{", "<"}
chunk_ends = {"(": ")", "[": "]", "{": "}", "<": ">"}
point_table = {")": 3, "]": 57, "}": 1197, ">": 25137}


def read_data(input_data):
    return [list(line) for line in input_data.splitlines()]


def run(input_data: str):
    lines = read_data(input_data)
    result = 0
    for line in lines:
        opening_brackets = []
        for char in line:
            if char in chunk_start:
                opening_brackets.append(char)
            else:
                expected = chunk_ends[opening_brackets.pop(-1)]
                if expected != char:
                    result += point_table[char]
                    break
    return result


if __name__ == "__main__":
    print(run(open("src/2021/data/days/10/data", "r").read()))
