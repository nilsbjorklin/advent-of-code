import re

bags: dict[str, list[str]] = {}


def read_data(input_data: str) -> None:
    global bags
    bags = {
        bag: re.compile(r"(\d+) (\w+ \w+)").findall(contains)
        for bag, contains in [
            line.split(" bags contain ") for line in input_data.splitlines()
        ]
    }


def run(input_data: str) -> int:
    read_data(input_data)
    return find(1, "shiny gold") - 1


def find(amount: int, bag_name: str) -> int:
    result = amount
    for contained_bag_amount, contained_bag in bags[bag_name]:
        result += find(
            int(contained_bag_amount) * amount,
            contained_bag,
        )
    return result


if __name__ == "__main__":
    print(run(open("data", "r").read()))
