def read_data(input_data):
    coordinates, folds = input_data.split("\n\n")
    line, num = folds.splitlines()[0].split("=")
    return {tuple(map(int, coord.split(","))) for coord in coordinates.splitlines()}, (line[-1], int(num))


def run(input_data):
    coordinates, (axis, value) = read_data(input_data)
    return len({calc_new_coord(axis, value, coordinate) for coordinate in coordinates} )

def calc_new_coord(axis, value, coordinate):
    x, y = coordinate
    if axis == "x":
        diff = x - value
        if diff > 0:
            x = value - diff
    else:
        diff = y - value
        if diff > 0:
            y = value - diff
    return (x, y)

if __name__ == "__main__":
    print(run(open("src/2021/data/days/13/data", "r").read()))
