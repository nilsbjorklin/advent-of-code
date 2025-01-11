def read_data(input_data):
    result = []
    for row in input_data:
        total, values = row.split(":")
        values = [int(num) for num in values.strip().split(" ")]
        result.append((int(total), values))
    return result


def calculate_values(target: int, values: list[int], total: int = 0) -> int:
    values_to_try: list[int] = []
    if not values:
        return target if target == total else 0
    elif total > target:
        return 0
    elif not total:
        values_to_try.append(values[0])
    else:
        values_to_try = [total + values[0], total * values[0]]
    for value in values_to_try:
        res = calculate_values(target, values[1:], value)
        if res:
            return res
    return 0


def run(input_data: list[str]):
    result = 0
    for target, values in read_data(input_data):
        result += calculate_values(target, values)
    return result


if __name__ == "__main__":
    print(run(open("src/2024/data/days/07/data", "r").readlines()))
