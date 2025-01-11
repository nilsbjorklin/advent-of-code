from functools import reduce
import re
str_nums = []
def read_data(input_data):
    result = []
    pattern = re.compile(r"one|two|three|four|five|six|seven|eight|nine|\d")
    for line in input_data.strip().splitlines():
        result.append(list(map(str_to_num, pattern.findall(line))))
    return result

def str_to_num(str):
    if str.isdigit():
        return int(str)
    else:
        match(str):
            case "one":
                return 1
            case "two":
                return 2
            case "three":
                return 3
            case "four":
                return 4
            case "five":
                return 5
            case "six":
                return 6
            case "seven":
                return 7
            case "eight":
                return 8
            case "nine":
                return 9

def run(input_data: list[str]):
    data = read_data(input_data)
    return reduce(lambda y, x: y + x[0]*10 + x[-1], data, 0)


if __name__ == "__main__":
    print(run(open("src/2024/data/days/01/data", "r").read()))
