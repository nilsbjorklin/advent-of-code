def run(input_data: list[str]) -> int:
    result = 0
        
    for line in input_data:
        num = 1
        min_val = int(line.split("-")[0])
        max_val = int(line.split("-")[1])
        while(num < pow(10, len(str(max_val)) // 2 + 1)):
            num_str = int(str(num) + str(num))
            if num_str >= min_val and num_str <= max_val:
                result += num_str
            num += 1
    return result

if __name__ == "__main__":
    file = open("src/2025/02/data", "r")
    lines = file.read().split(",")
    print(run(lines))