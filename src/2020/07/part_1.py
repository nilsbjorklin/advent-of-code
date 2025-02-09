import re
from collections import defaultdict
from functools import lru_cache

contained_bags = defaultdict(list)


def read_data(input_data: str) -> None:
    global contained_bags
    bag_contains = {
        bag: re.compile(r"\d+ (\w+ \w+)").findall(contains)
        for bag, contains in [
            line.split(" bags contain ") for line in input_data.splitlines()
        ]
    }
    for bag, contains in bag_contains.items():
        for color in contains:
            contained_bags[color].append(bag)


def run(input_data: str) -> int:
    read_data(input_data)
    return len(find("shiny gold"))


@lru_cache
def find(bag_name) -> set[str]:
    bags = set()
    for container in contained_bags[bag_name]:
        bags.add(container)
        bags.update(find(container))
    return bags


if __name__ == "__main__":
    print(run(open("data", "r").read()))
