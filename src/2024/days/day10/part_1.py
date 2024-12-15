import numpy as np

data: list[list[int]] = []
width = height = 0
directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def read_data(input_data):
    global data
    global width
    global height
    for row in input_data:
        result_row = []
        for value in row.strip():
            result_row.append(int(value))
        data.append(result_row)
    width = len(data[0])
    height = len(data)


def run(input_data: list[str]):
    read_data(input_data)
    result_array = array_step().flatten()
    result = 0
    for value in result_array:
        if value is not None:
            result += value.size
    return result


def comparator(x):
    print(x)


def array_step(prev_array=None, value=9):
    if prev_array is None:
        prev_array = np.full((width, height), None)
        for idx, (x, y) in enumerate(search_for(value)):
            prev_array[x][y] = np.array(idx)
        return array_step(prev_array, value - 1)
    res = np.full((width, height), None)
    locations = search_for(value)
    for x, y in locations:
        for x_dir, y_dir in directions:
            new_x = int(x + x_dir)
            new_y = int(y + y_dir)
            if 0 <= new_x < width and 0 <= new_y < height:
                if prev_array[new_x][new_y] is not None:
                    if res[x][y] is None:
                        res[x][y] = prev_array[new_x][new_y]
                    else:
                        res[x][y] = np.unique(np.append(res[x][y], prev_array[new_x][new_y]))
    if value != 0:
        return array_step(res, value - 1)
    else:
        return res


def search_for(value):
    values = np.array(data)
    search_result = np.where(values == value)
    search_result = np.array(search_result).T
    return search_result


if __name__ == '__main__':
    print(run(open('../../data/days/10/data', 'r').readlines()))
