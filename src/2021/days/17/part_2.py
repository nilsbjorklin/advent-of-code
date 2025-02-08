import re
from collections import defaultdict

min_x_target = 0
max_x_target = 0
min_y_target = 0
max_y_target = 0


def read_data(line):
    global min_x_target, max_x_target, min_y_target, max_y_target
    pattern = re.compile(r"-?\d+")
    x, y = line.split("x")[1].split("y")
    print(x, y)
    x = list(map(int, pattern.findall(x)))
    y = list(map(int, pattern.findall(y)))
    min_x_target = min(*x)
    max_x_target = max(*x)
    min_y_target = min(*y)
    max_y_target = max(*y)


def run(input_data):
    read_data(input_data)

    step_to_y_velocities = defaultdict(list)
    for y_velocity in range(-abs(min_y_target), abs(min_y_target) + 1):
        for step in valid_y_steps(y_velocity):
            step_to_y_velocities[step].append(y_velocity)

    step_to_x_velocities = defaultdict(list)
    for x_velocity in range(min(0, min_x_target), max(0, max_x_target) + 1):
        for step in valid_x_steps(x_velocity, max(step_to_y_velocities.keys())):
            step_to_x_velocities[step].append(x_velocity)

    result = set()
    for step in step_to_x_velocities.keys():
        if step in step_to_y_velocities:
            for x_value in step_to_x_velocities[step]:
                for y_value in step_to_y_velocities[step]:
                    result.add((x_value, y_value))
    return len(result)


def valid_y_steps(y_velocity):
    valid_steps = []
    end_step = 0
    y_pos = 0
    while y_pos > min_y_target:
        y_pos = 0
        for step in range(end_step):
            y_pos += y_velocity - step
        if min_y_target <= y_pos <= max_y_target:
            valid_steps.append(end_step)
        end_step += 1
    return valid_steps


def valid_x_steps(x_velocity, max_step):
    x_pos = 0
    valid_steps = []
    step = 0
    while x_velocity != 0:
        x_pos += x_velocity
        step += 1
        if x_velocity < 0:
            if x_pos < min_x_target:
                break
        elif x_pos > max_x_target:
            break
        elif min_x_target <= x_pos <= max_x_target:
            valid_steps.append(step)
        if x_velocity > 0:
            x_velocity -= 1
        else:
            x_velocity += 1
    if x_velocity == 0 and min_x_target <= x_pos <= max_x_target:
        return valid_steps + [step for step in range(step + 1, max_step + 1)]
    return valid_steps


if __name__ == "__main__":
    print(run(open("data", "r").read()))
