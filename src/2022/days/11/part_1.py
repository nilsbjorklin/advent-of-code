from collections import defaultdict
from operator import add, mul
import re

item_lists = []
inspections = defaultdict(lambda: 0)


def throw_item(index, sign, second, mod, if_true, if_false):
    inspections[index] += 1
    first = item_lists[index].pop(0)
    second = first if second == "old" else int(second)
    item = (add(first, second) if sign == "+" else mul(first, second)) // 3
    item_lists[if_true if item % mod == 0 else if_false].append(item)


def read_data(input_data):
    monkeys = []
    monkey_pattern = re.compile(
        r"\n\D+(\d+(?:, \d+)*)\n[^=]+= \w{3} ((?:.) (?:old|new|\d+))\D+(\d+)\D+(\d+)\D+(\d+)"
    )
    digits = re.compile(r"(\d+)")
    for items, op, mod, if_true, if_false in monkey_pattern.findall(input_data):
        item_lists.append(list(map(int, digits.findall(items))))
        monkeys.append((*op.split(" "), int(mod), int(if_true), int(if_false)))
    return monkeys


def run(input_data, rounds):
    monkeys = read_data(input_data)
    for index in range(rounds * len(monkeys)):
        monkey_index = index % len(monkeys)
        while len(item_lists[monkey_index]) != 0:
            throw_item(monkey_index, *monkeys[monkey_index])
    return mul(*sorted(inspections.values())[-2:])


if __name__ == "__main__":
    print(run(open("src/2022/data/days/11/data", "r").read(), 20))
