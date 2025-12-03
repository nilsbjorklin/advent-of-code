def run(input_data: list[str], debug:bool=False) -> int:
    position = 50
    result = 0
    if debug:
        print(' - The dial starts by pointing at 50.')
    for line in input_data:
        move = parse_line(line.strip())
        target_position = position + move
        while position < target_position:
            position += 1
            if position % 100 == 0:
                result += 1
        while position > target_position:
            position -= 1
            if position % 100 == 0:
                result += 1
        if debug:
            print(f' - The dial is rotated {line.strip()} to point at {position % 100}.')
    return result

def parse_line(line: str) -> int:
    return -int(line[1:]) if line.startswith('L') else int(line[1:])

if __name__ == "__main__":
    example_lines = open("src/2025/01/data_example", "r").readlines()
    example_result = run(example_lines, debug=True)
    if( example_result != 6):
        raise ValueError(f'Expected example result to be 6 but got {example_result}')
    lines = open("src/2025/01/data", "r").readlines()
    print('Result:', run(lines))