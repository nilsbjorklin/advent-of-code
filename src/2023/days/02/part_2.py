from collections import defaultdict
import re


def read_data(input_data):
    games = {}
    pattern = re.compile(r"(\d+) (\w+)")
    game_id = re.compile(r"Game (\d+):")
    for line in input_data.strip().splitlines():
        game = defaultdict(lambda: 0)
        for num, color in pattern.findall(line):
            game[color] = max(game[color], int(num))
        games[int(game_id.findall(line)[0])] = game
    return games

def game_possible(game, cubes):
    for k, v in game.items():
            if k not in cubes or cubes[k] < v:
                return False
    return True

def run(input_data: list[str], cubes):
    games = read_data(input_data)
    result = 0
    for index, game in games.items():
        if game_possible(game, cubes):
            result += index
    return result


if __name__ == "__main__":
    print(run(open("src/2023/data/days/02/data", "r").read(), {"red": 12, "green": 13, "blue": 14}))
