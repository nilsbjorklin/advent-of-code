import re


def read_data(input_data):
    pattern = re.compile(r"(\d+)")
    race = []
    for row in input_data.strip().splitlines():
        race.append(int("".join(pattern.findall(row))))
    return tuple(race)


def run(input_data: list[str]):
    time, record = read_data(input_data)
    return race_time(time, record)


def race_time(time, record):
    for speed in range(1, time):
        distance = speed * (time - speed)
        if distance > record:
            return time - speed * 2 + 1
    return 0


if __name__ == "__main__":
    print(run(open("src/2023/data/days/06/data", "r").read()))
