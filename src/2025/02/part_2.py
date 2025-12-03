def run(input_data: list[str], debug:bool=False) -> int:
    result = 0
        
    for line in input_data:
        result_for_line:set[int] = set()
        for repeats in range(2, line.__len__() - 1):
            result_for_line.update(check_num_repeats(line, repeats))
        if debug:
            print(f'- {line.strip()} has invalid values: {", ".join(map(str, result_for_line))}')
        result += sum(result_for_line)
    return result

def check_num_repeats(line:str, repeats: int) -> set[int]:
    invalid_values:set[int] = set()
    num = 1
    repeat_num = int(str(num) * repeats)
    min_val = int(line.split("-")[0])
    max_val = int(line.split("-")[1])
    while(repeat_num <= max_val):
        if repeat_num >= min_val:
            invalid_values.add(repeat_num)
        num += 1
        repeat_num = int(str(num) * repeats)
    return invalid_values

if __name__ == "__main__":
    example_lines = open("src/2025/02/data_example", "r").read().split(",")
    example_result = run(example_lines, debug=True)
    if( example_result != 4174379265):
        raise ValueError(f'Expected example result to be 4174379265 but got {example_result}')
    lines = open("src/2025/02/data", "r").read().split(",")
    print('Result:', run(lines))