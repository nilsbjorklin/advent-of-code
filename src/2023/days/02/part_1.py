from collections import defaultdict
from functools import reduce
import re


def read_data(input_data):
    games = []
    pattern = re.compile(r"(\d+) (green|red|blue)")
    for line in input_data.strip().splitlines():
        game = defaultdict(lambda: 0)
        for num, color in pattern.findall(line):
            game[color] = max(game[color], int(num))
        games.append(game)
    return games


def run(input_data: list[str]):
    games = read_data(input_data)
    return reduce(
        lambda total, game: total + reduce(lambda x, y: x * y, game.values(), 1),
        games,
        0,
    )


if __name__ == "__main__":
    print(run(open("src/2023/data/days/02/data", "r").read()))
