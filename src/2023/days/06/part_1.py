
import re


def read_data(input_data):
    pattern = re.compile(r"(\d+)")
    lines = [list(map(int, pattern.findall(row))) for row in input_data.strip().splitlines()]
    return [race for race in zip(*lines)]
    


def run(input_data: list[str]):
    races = read_data(input_data)
    result = None
    for race in races:
        if result is None:
            result = race_time(*race)
        else:
            result *= race_time(*race)
    return result

def race_time(time, record):
    first_win = 0
    last_win = 0
    for button_time in range(1, time):
        speed = button_time
        time_left = time - button_time
        distance = speed * time_left
        if distance > record:
            if first_win == 0:
                first_win = button_time - 1
                last_win = button_time
            else:
                last_win = button_time
    return last_win - first_win
    
if __name__ == "__main__":
    print(run(open("src/2023/data/days/06/data", "r").read()))
