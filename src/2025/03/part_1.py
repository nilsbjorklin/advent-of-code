def run(input_data: list[str]) -> int:
    result = 0
        
    for line in input_data:
        firstVal = 0
        secondVal = 0
        for index in range(line.strip().__len__()):
            num = int(line[index])
            if num > firstVal and index != line.strip().__len__() - 1:
                firstVal = num
                secondVal = 0
            elif num > secondVal:
                secondVal = num
        result += firstVal * 10 + secondVal
    return result

if __name__ == "__main__":
    example_lines = open("src/2025/03/data_example", "r").readlines()
    example_result = run(example_lines)
    if( example_result != 357):
        raise ValueError(f'Expected example result to be 357 but got {example_result}')
    lines = open("src/2025/03/data", "r").readlines()
    print('Result:', run(lines))