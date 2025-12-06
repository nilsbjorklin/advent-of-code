def parse(lines: str) -> list[tuple[int, int]]:
    ranges = lines.split('\n\n')[0]
        
    return [(start, end) for start, end in [tuple(map(int, range.strip().split('-'))) for range in ranges.splitlines()]]

def run(lines: str) -> int:
    ranges = combine_ranges(parse(lines))
    
    return sum([end + 1 - start for start, end in ranges])

def combine_ranges(ranges: list[tuple[int, int]]) -> list[tuple[int, int]]:
    sorted_ranges = sorted(ranges, key=lambda r: r[0])
    combined_ranges: list[tuple[int, int]] = []
    current_range = sorted_ranges[0]
    for next_range in sorted_ranges[1:]:
        if current_range[1] > next_range[0] - 1:
            current_range = (current_range[0], max(current_range[1], next_range[1]))
        else:
            combined_ranges.append(current_range)
            current_range = next_range
    combined_ranges.append(current_range)
    return combined_ranges

if __name__ == "__main__":
    example_lines = open("src/2025/05/data_example", "r").read()
    example_result = run(example_lines)
    if( example_result != 14):
        raise ValueError(f'Expected example result to be 14 but got {example_result}')
    lines = open("src/2025/05/data", "r").read()
    print('Result:', run(lines))