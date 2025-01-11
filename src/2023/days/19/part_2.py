from collections import deque
from copy import deepcopy
from functools import reduce
import re


def read_data(input_data):
    workflows = {}
    for row in input_data.split("\n\n")[0].splitlines():
        name, rules = re.compile(r"(\w{2,3})\{(.*)\}").findall(row)[0]
        rules = rules.split(",")
        workflows[name] = [
            list(re.compile(r"(\w+)([<>])(\d+):(\w+)").findall(rule)[0])
            for rule in rules[:-1]
        ]
        workflows[name].append(rules[-1:])

    return workflows


def run(input_data):
    workflows = read_data(input_data)
    start_part_rating = {"x": (1, 4000), "m": (1, 4000), "a": (1, 4000), "s": (1, 4000)}
    next_flows = deque([["in", start_part_rating]])
    result = 0
    while len(next_flows) != 0:
        workflow_name, part_rating = next_flows.popleft()
        if workflow_name == "A":
            value_ranges = [1 + (v2 - v1) for v1, v2 in part_rating.values()]
            result += reduce(lambda a, b: a * b, value_ranges, 1)
        elif workflow_name != "R":
            next_flows += run_instruction(part_rating, workflows[workflow_name])
    return result


def run_instruction(part_rating, instructions):
    paths = []
    for instruction in instructions:
        if len(instruction) == 1:
            paths.append((instruction[0], part_rating))
            return paths
        input_name, condition, limit, output = instruction
        start, end = part_rating[input_name]
        limit = int(limit)

        if start < limit < end:
            match_part_rating = deepcopy(part_rating)
            if condition == ">":
                match_part_rating[input_name] = (limit + 1, end)
                part_rating[input_name] = (start, limit)
            if condition == "<":
                match_part_rating[input_name] = (start, limit - 1)
                part_rating[input_name] = (limit, end)
            paths.append((output, match_part_rating))
    return paths


if __name__ == "__main__":
    print(run(open("src/2023/data/days/19/data", "r").read()))
