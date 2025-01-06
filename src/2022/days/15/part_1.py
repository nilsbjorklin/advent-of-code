import re


def read_data(input_data, row_num):
    pattern = re.compile(r"x=(-?\d+), y=(-?\d+)")
    return [
        [tuple(map(int, pos)) for pos in pattern.findall(row)]
        for row in input_data.splitlines()
    ]


def run(input_data, row_num):
    pairs = read_data(input_data, row_num)
    excluded_in_row = set()
    beacons_in_row = set()
    for (sensor_x, sensor_y), (beacon_x, beacon_y) in pairs:
        steps_left = abs(sensor_x - beacon_x) + abs(sensor_y - beacon_y)
        steps_left -= abs(row_num - sensor_y)
        while steps_left >= 0:
            excluded_in_row.add(sensor_x + steps_left)
            excluded_in_row.add(sensor_x - steps_left)
            steps_left -= 1
        if beacon_y == row_num:
            beacons_in_row.add(beacon_x)
    return len(excluded_in_row.difference(beacons_in_row))


if __name__ == "__main__":
    print(run(open("src/2022/data/days/15/data", "r").read(), 2000000))
