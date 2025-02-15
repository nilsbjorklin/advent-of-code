def read_data(input_data: str) -> (int, list):
    earliest, schedule = input_data.splitlines()
    return int(earliest), [int(num) for num in schedule.split(",") if num != "x"]


def run(input_data: str) -> int:
    earliest, schedule = read_data(input_data)
    values = {calc_wait(earliest, num): num for num in schedule}
    min_wait = min(values.keys())
    return min_wait * values[min_wait]


def calc_wait(earliest, num):
    times = earliest // num + 1
    num *= times
    return num - earliest


if __name__ == "__main__":
    print(run(open("data", "r").read()))
