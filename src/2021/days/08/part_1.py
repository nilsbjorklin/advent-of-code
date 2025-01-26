valid_lens = {2, 4, 3, 7}
def read_data(input_data):
    values = []
    for line in input_data.splitlines():
        for value in [len(values) for values in line.split("|")[1].strip().split(" ")]:
            values.append(value)
    return values


def run(input_data: str):
    values = read_data(input_data)
    return sum([1 for value in values if value in valid_lens])

if __name__ == "__main__":
    print(run(open("src/2021/data/days/08/data", "r").read()))
