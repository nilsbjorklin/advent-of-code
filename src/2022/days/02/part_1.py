score = {"X": 1, "Y": 2, "Z": 3, "A": 1, "B": 2, "C": 3}


def read_data(input_data):
    games = []
    for row in input_data.splitlines():
        games.append(tuple(map(lambda x: score[x], row.split(" "))))
    return games


def run(input_data: list[str]):
    games = read_data(input_data)
    score = 0
    for opponent, you in games:
        match (you - opponent):
            case 0:
                score += you + 3
            case -2 | 1:
                score += you + 6
            case 2 | -1:
                score += you + 0
    return score


if __name__ == "__main__":
    print(run(open("src/2022/data/days/02/data", "r").read()))
