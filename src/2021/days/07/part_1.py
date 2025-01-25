from functools import reduce


def read_data(input_data):
    return sorted(list(map(int, input_data.split(","))))


def run(input_data: str):
    crabs = read_data(input_data)
    return reduce(lambda res, val: res + abs(val - crabs[len(crabs)//2]), crabs, 0)

if __name__ == "__main__":
    print(run(open("src/2021/data/days/07/data", "r").read()))
