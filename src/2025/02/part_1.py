def run(input_data: list[str]) -> int:
    result = 0
        
    for line in input_data:
        num = 1
        repeat_num = int(str(num) + str(num))
        min_val = int(line.split("-")[0])
        max_val = int(line.split("-")[1])
        while(repeat_num <= max_val):
            if repeat_num >= min_val:
                result += repeat_num
            num += 1
            repeat_num = int(str(num) + str(num))
    return result

if __name__ == "__main__":
    example_lines = open("src/2025/02/data_example", "r").read().split(",")
    example_result = run(example_lines)
    if( example_result != 1227775554):
        raise ValueError(f'Expected example result to be 1227775554 but got {example_result}')
    lines = open("src/2025/02/data", "r").read().split(",")
    print('Result:', run(lines))