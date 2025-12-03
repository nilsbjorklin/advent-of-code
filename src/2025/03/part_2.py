def run(input_data: list[str], length: int) -> int:
    result = 0
        
    for line in input_data:
        start_index = 0
        numArray: list[str] = []
        max_index = line.strip().__len__()
        for index in range(length):
            [bestVal, bestIndex] = find_best_number(line, start_index, max_index + index + 1 - length)
            numArray.append(str(bestVal))
            start_index = bestIndex + 1
        result += int(''.join(numArray))
    return result

def find_best_number(line: str, startIndex: int, max_index: int) -> tuple[int, int]:
    bestVal = 0
    bestIndex = startIndex
    for index in range(startIndex, max_index ):
        num = int(line[index])
        if num > bestVal:
            bestVal = num
            bestIndex = index
    return bestVal, bestIndex
if __name__ == "__main__":
    example_lines = open("src/2025/03/data_example", "r").readlines()
    example_result = run(example_lines, 12)
    if( example_result != 3121910778619):
        raise ValueError(f'Expected example result to be 3121910778619 but got {example_result}')
    lines = open("src/2025/03/data", "r").readlines()
    print('Result:', run(lines, 12))