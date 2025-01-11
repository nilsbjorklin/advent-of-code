from collections import defaultdict
import re


def read_data(input_data):
    cards = []
    pattern = re.compile(r"\d+")
    for row in input_data.strip().splitlines():
        winning, numbers = row.split("|")
        winning = winning.split(":")[1]
        cards.append((set(pattern.findall(winning)), set(pattern.findall(numbers))))
    return cards


def run(input_data: list[str]):
    cards = read_data(input_data)
    result = defaultdict(lambda:1)
    for index, card in enumerate(cards):
        multiplier = result[index]
        winning, numbers = card
        numbers_in_both = winning.intersection(numbers)
        if numbers_in_both:
            for i in range(index + 1, index + len(numbers_in_both) + 1):
                result[i] += multiplier
    return sum(result.values())


if __name__ == "__main__":
    print(run(open("src/2023/data/days/04/data", "r").read()))
