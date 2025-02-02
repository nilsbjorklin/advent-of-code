def read_data(input_data):
    coordinates, folds = input_data.split("\n\n")
    folds = [fold.split("=") for fold in folds.splitlines()]
    folds = [(line[-1], int(num)) for line, num in folds]
    return {tuple(map(int, coord.split(","))) for coord in coordinates.splitlines()}, folds


def run(input_data):
    coordinates, folds = read_data(input_data)
    y_max = x_max = 999999
    for axis, value in folds:
        coordinates = {calc_new_coord(axis, value, *coordinate) for coordinate in coordinates}
        if axis == "x":
            x_max = value
        else:
            y_max = value
    print_grid(coordinates, y_max, x_max)

def calc_new_coord(axis, value, x, y):
    if axis == "x" and x > value:
        x = value - (x - value)
    elif axis == "y" and y > value:
        y = value - (y - value)
    return (x, y)

def print_grid(coordinates, y_max, x_max):
    for y in range(y_max):
        for x in range(x_max):
            if (x, y) in coordinates:
                print("O", end="")
            else:
                print(" ", end="")
        print()
    print()


if __name__ == "__main__":
    run(open("src/2021/data/days/13/data", "r").read())
