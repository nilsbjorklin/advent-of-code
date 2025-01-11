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
    result = 0
    for winning, numbers in cards:
        numbers_in_both = winning.intersection(numbers)
        if numbers_in_both:
            number_of_matches = len(numbers_in_both) - 1
            result += 2**number_of_matches
    return result


if __name__ == "__main__":
    print(run(open("src/2023/data/days/04/data", "r").read()))
