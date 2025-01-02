def read_data(input_data):
    return input_data.split(",")

def run(input_data):
    rows = read_data(input_data)
    total_sum = 0
    for row in rows:
        result = 0
        for char in row:
            result += ord(char)
            result *= 17
            result = result % 256
        total_sum += result
    return total_sum
            

if __name__ == "__main__":
    print(run(open("src/2023/data/days/15/data", "r").read()))
