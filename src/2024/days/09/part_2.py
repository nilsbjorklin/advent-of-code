from copy import deepcopy


def read_data(input_data):
    input_data = input_data[0].strip()
    file_counter = 0
    blocks = []

    for i, val in enumerate(input_data):
        if i % 2 == 0:
            blocks.append([file_counter, int(val)])
            file_counter += 1
        elif i % 2 == 1:
            blocks.append([None, int(val)])
    return blocks


def find_file(blocks, start):
    max_size = blocks[start][1]
    end = len(blocks) - 1
    while start < end:
        if blocks[end][0] is not None and blocks[end][1] <= max_size:
            return end
        else:
            end -= 1
    return None


def run(input_data: list[str]):
    blocks = read_data(input_data)
    result_blocks = []
    start = 0
    while start < len(blocks):
        if blocks[start][0] is not None:
            result_blocks.append(blocks.pop(start))
        elif blocks[start][1] == 0:
            del blocks[start]
        else:
            idx = find_file(blocks, start)
            if idx:
                elem = deepcopy(blocks[idx])
                blocks[idx][0] = None
                result_blocks.append(elem)
                blocks[start][1] -= elem[1]
            else:
                result_blocks.append(blocks.pop(start))

    result = 0
    file_number = 0
    for block_value, block_size in result_blocks:
        for i in range(block_size):
            if block_value is not None:
                result += file_number * block_value
            file_number += 1
    return result


if __name__ == "__main__":
    print(run(open("src/2024/data/days/09/data", "r").readlines()))
