def parse(lines: str) -> tuple[list[tuple[int, ...]], list[int]]:
    ranges, values = lines.split('\n\n')
    return [tuple(map(int, range.strip().split('-'))) for range in ranges.splitlines()], [int(value) for value in values.splitlines()]

def run(lines: str) -> int:
    ranges, values = parse(lines)
    return len([value for value in values if any(start <= value <= end for (start, end) in ranges)])

if __name__ == "__main__":
    example_lines = open("src/2025/05/data_example", "r").read()
    example_result = run(example_lines)
    if( example_result != 3):
        raise ValueError(f'Expected example result to be 3 but got {example_result}')
    lines = open("src/2025/05/data", "r").read()
    print('Result:', run(lines))