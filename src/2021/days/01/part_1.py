def read_data(input_data):
    return [int(row.strip()) for row in input_data.splitlines()] 

def run(input_data: str):
    values = read_data(input_data)
    return sum([1 if values[index] < values[index + 1] else 0 for index in range(len(values) - 1)])
        


if __name__ == "__main__":
    print(run(open("src/2021/data/days/01/data", "r").read()))
