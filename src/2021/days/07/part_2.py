from functools import lru_cache


def read_data(input_data):
    return sorted(list(map(int, input_data.split(","))))


def run(input_data: str):
    crabs = read_data(input_data)
    best_value = None
    for target in range(crabs[0], crabs[-1]):
        value = sum([crab_cost(abs(crab - target)) for crab in crabs])
        if best_value is not None and value > best_value:
            return best_value
        best_value = value


@lru_cache
def crab_cost(steps):
    return sum(range(1, steps + 1))


if __name__ == "__main__":
    print(run(open("src/2021/data/days/07/data", "r").read()))
