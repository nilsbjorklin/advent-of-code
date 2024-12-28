from functools import cache

keypad = {}


def read_data(input_data: str):
    numerical_grid = [
        ["7", "8", "9"],
        ["4", "5", "6"],
        ["1", "2", "3"],
        [" ", "0", "A"],
    ]
    directional_grid = [[" ", "^", "A"], ["<", "v", ">"]]

    numerical_keypad = {
        val: complex(x, y)
        for y, row in enumerate(numerical_grid)
        for x, val in enumerate(row)
    }
    directional_keypad = {
        val: complex(x, y)
        for y, row in enumerate(directional_grid)
        for x, val in enumerate(row)
    }

    global keypad
    for k, v in numerical_keypad.items():
        keypad[k] = v - numerical_keypad["A"]
    for k, v in directional_keypad.items():
        keypad[k] = v - directional_keypad["A"]
    return input_data.strip().splitlines()


@cache
def best_move(start, end):
    distance = keypad[end] - keypad[start]
    change_x = int(distance.real)
    change_y = int(distance.imag)
    x_moves = ("<" * -change_x) + (">" * change_x)
    y_moves = ("^" * -change_y) + ("v" * change_y)

    test_pos = -2 - keypad[start]
    if change_x > 0 or test_pos == change_x:
        if test_pos != change_y * 1j:
            return y_moves + x_moves
    return x_moves + y_moves


@cache
def sum_for_part(code, depth, result=0):
    if depth < 0:
        return len(code)
    prev = "A"
    for i, c in enumerate(code):
        result += sum_for_part(best_move(prev, c) + "A", depth - 1)
        prev = code[i]
    return result


def run(input_data, max_depth):
    expected_output_list = read_data(input_data)
    result = 0
    for output in expected_output_list:
        result += int(output[:3]) * sum_for_part(output, max_depth)
    return result


if __name__ == "__main__":
    print(run(open("src/2024/data/days/21/data", "r").read(), max_depth=2))
