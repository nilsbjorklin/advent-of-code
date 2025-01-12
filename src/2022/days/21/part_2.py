from functools import lru_cache
import re

monkey_actions = {}


def read_data(input_data):
    pattern = re.compile(r"(\w+) ([\+\-\*\/]) (\w+)")
    global monkey_actions
    for row in input_data.splitlines():
        name, action = row.split(":")
        actions = pattern.findall(action)
        monkey_actions[name] = actions[0] if len(actions) != 0 else int(action)


def run(input_data):
    read_data(input_data)
    first, _, second = monkey_actions["root"]
    first, second = calculate_monkey(first), calculate_monkey(second)
    values, target = (first, second) if type(first) != int else (second, first)

    for index in range(len(values)):
        name = values[index]
        if name == "humn":
            return target
        first, operator, second = monkey_actions[name]
        if first == values[index + 1]:
            first, second = None, calculate_monkey(second)
        else:
            first, second = calculate_monkey(first), None
        target = process_values_backwards(first, second, operator, target)


@lru_cache
def process_values_backwards(first, second, operator, target):
    match operator:
        case "+":
            return target - (first if second is None else second)
        case "-":
            return target + second if first is None else first - target
        case "*":
            return target // (first if second is None else second)
        case "/":
            return (
                target * second
                if first is None
                else first + 1 if target == 0 else first // target
            )
        case __:
            raise (ValueError(f"Unknown operator {operator}"))


@lru_cache
def calculate_monkey(name):
    actions = monkey_actions[name]
    if type(actions) != tuple:
        return [name] if name == "humn" else actions

    first = calculate_monkey(actions[0])
    second = calculate_monkey(actions[2])

    if type(first) == type(second) and type(first) == int:
        return process_values(first, second, actions[1])
    else:
        result = [name]
        result += first if type(first) != int else []
        result += second if type(second) != int else []
        return result


@lru_cache
def process_values(first, second, operator):
    match operator:
        case "+":
            return first + second
        case "-":
            return first - second
        case "*":
            return first * second
        case "/":
            return first // second
        case __:
            raise (ValueError(f"Unknown operator {operator}"))


if __name__ == "__main__":
    print(run(open("src/2022/data/days/21/data", "r").read()))
