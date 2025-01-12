from functools import lru_cache
import re

monkey_actions = {}


def read_data(input_data):
    pattern = re.compile(r"(\w+) ([\+\-\*\/]) (\w+)")
    global monkey_actions
    for row in input_data.splitlines():
        name, action = row.split(":")
        actions = pattern.findall(action)
        if len(actions) != 0:
            monkey_actions[name] = actions[0]
        else:
            monkey_actions[name] = int(action)


def run(input_data):
    read_data(input_data)
    return calculate_monkey("root")


@lru_cache
def calculate_monkey(name):
    actions = monkey_actions[name]
    if type(actions) != tuple:
        return actions
    return process_values(
        calculate_monkey(actions[0]), calculate_monkey(actions[2]), actions[1]
    )


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


if __name__ == "__main__":
    print(run(open("src/2022/data/days/21/data", "r").read()))
