import re

min_y_target = 0
max_y_target = 0


def read_data(line):
    global min_y_target, max_y_target
    pattern = re.compile(r"-?\d+")
    y = list(map(int, pattern.findall(line.split("y")[1])))
    min_y_target = min(*y)
    max_y_target = max(*y)


def run(input_data):
    read_data(input_data)
    y_velocity = 1
    max_y = 0
    for i in range(abs(min_y_target)):
        result = valid_y_steps(y_velocity)
        if result > max_y:
            max_y = result
        y_velocity += 1
    return max_y


def valid_y_steps(y_velocity):
    max_y = 0
    end_step = 1
    y_pos = 0
    while y_pos > min_y_target:
        y_pos = 0
        for step in range(end_step):
            y_pos += y_velocity - step
        max_y = max(max_y, y_pos)
        if min_y_target <= y_pos <= max_y_target:
            return max_y
        end_step += 1
    return 0


if __name__ == "__main__":
    # print(run("target area: x=20..30, y=-10..-5"))
    print(run(open("data", "r").read()))
