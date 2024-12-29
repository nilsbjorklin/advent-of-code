import itertools
import re

directions = set(
        map(lambda xy: xy[0] + xy[1], itertools.product([1, 0, -1], [1j, 0, -1j]))
    )
width = height = 0
def read_data(input_data):
    digits = {}
    digit_values = {}
    gears = set()
    pattern = re.compile(r"\d+|[*]")
    digit_id = 0
    for y, row in enumerate(input_data.strip().splitlines()):
        for digit_match in pattern.finditer(row):
            if digit_match.group(0).isdigit():
                for x in range(*digit_match.span(0)):
                    digits[complex(x, y)] = digit_id
                digit_values[digit_id] = int(digit_match.group(0))
                digit_id +=1                
            else:
                gears.add(complex(digit_match.span(0)[0], y))
    return digits, digit_values, gears


def run(input_data: list[str]):
    digits, digit_values, gears = read_data(input_data)
    result = 0
    invalid_gears = []
    for gear in gears:
        neighbor_ids = []
        for direction in directions:
            near_pos = gear + direction
            if near_pos in digits and digits[near_pos] not in neighbor_ids:
                neighbor_ids.append(digits[near_pos])
        if len(neighbor_ids) == 2:
            neighbor_ids = list(neighbor_ids)
            first = digit_values[neighbor_ids[0]]
            second = digit_values[neighbor_ids[1]]
            result += first * second
        else:
            invalid_gears.append(gear)
    return result

if __name__ == "__main__":
   print(run(open("src/2023/data/days/03/data", "r").read()))
