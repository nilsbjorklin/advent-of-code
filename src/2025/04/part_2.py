import itertools

def parse_grid(lines: list[str]) -> set[complex]:
    grid: set[complex] = set()
    for row_index in range(len(lines)):
        line = lines[row_index].strip()
        for col_index in range(len(line)):
            if line[col_index] == '@':
                grid.add(complex(row_index, col_index))
    return grid

def run(input_data: list[str], debug: bool=False) -> int:
    directions:list[complex] = [complex(x, y) for (x, y) in list(itertools.product({1, -1, 0}, repeat=2))]
    grid = parse_grid(input_data)
    remaining_rolls = grid.copy()
    result = 0
    if debug:
        print(f'Starting with {len(remaining_rolls)} rolls')
    while(True):
        new_remaining_rolls = [value for value in remaining_rolls if not roll_is_valid(value, remaining_rolls, directions)]
        result += len(remaining_rolls) - len(new_remaining_rolls)
        if debug:
            print(f'Removed {len(remaining_rolls) - len(new_remaining_rolls)} rolls, remaining rolls: {len(new_remaining_rolls)}')
        if(len(new_remaining_rolls) == len(remaining_rolls)):
            return len(grid) - len(remaining_rolls)
        remaining_rolls = new_remaining_rolls

def roll_is_valid(value: complex, grid: set[complex], directions: list[complex]) -> bool:
    count = 0
    for direction in directions:
        if value + direction in grid:
            count += 1
        if count > 4:
            return False
    return True
        

if __name__ == "__main__":
    example_lines = open("src/2025/04/data_example", "r").readlines()
    example_result = run(example_lines, debug=True)
    if( example_result != 43):
        raise ValueError(f'Expected example result to be 43 but got {example_result}')
    lines = open("src/2025/04/data", "r").readlines()
    print('Result:', run(lines))