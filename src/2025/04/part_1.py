import itertools


def parse_grid(lines: list[str]) -> set[complex]:
    grid: set[complex] = set()
    for row_index in range(len(lines)):
        line = lines[row_index].strip()
        for col_index in range(len(line)):
            if line[col_index] == '@':
                grid.add(complex(row_index, col_index))
    return grid

def run(input_data: list[str]) -> int:
    directions:list[complex] = [complex(x, y) for (x, y) in list(itertools.product({1, -1, 0}, repeat=2))]
    grid = parse_grid(input_data)
    return sum([roll_is_valid(value, grid, directions) for value in grid])

def roll_is_valid(value: complex, grid: set[complex], directions: list[complex]) -> int:
    count = 0
    for direction in directions:
        if value + direction in grid:
            count += 1
        if count > 4:
            return 0
    return 1
        

if __name__ == "__main__":
    example_lines = open("src/2025/04/data_example", "r").readlines()
    example_result = run(example_lines)
    if( example_result != 13):
        raise ValueError(f'Expected example result to be 13 but got {example_result}')
    lines = open("src/2025/04/data", "r").readlines()
    print('Result:', run(lines))