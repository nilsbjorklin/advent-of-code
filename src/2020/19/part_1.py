import re
from functools import lru_cache

rules = {}


def read_data(input_data: str) -> list:
    global rules
    pattern = re.compile(r"(\w+|\d+|\|)")
    rule_data, lines = input_data.split("\n\n")
    for rule_line in rule_data.splitlines():
        matches = pattern.findall(rule_line)
        rules[int(matches[0])] = matches[1:]
    return lines.splitlines()


def run(input_data: str) -> int:
    lines = read_data(input_data)
    return len([line for line in lines if line in rule()])


@lru_cache
def rule(number=0):
    values = rules[number]
    results = set()
    part_results = {""}
    for index in range(len(values)):
        val = values[index]
        if val == "|":
            results.update(part_results)
            part_results = {""}
        else:
            new_parts = rule(int(val)) if val.isdigit() else {val}
            new_part_results = set()
            for new_part in new_parts:
                for part_result in part_results:
                    new_part_results.add(part_result + new_part)
            part_results = new_part_results

    results.update(part_results)
    return results


if __name__ == "__main__":
    print(run(open("data", "r").read()))
