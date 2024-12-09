def read_data(input_data):
    input_data = input_data[0].strip()
    file_counter = 0
    blocks = []

    for i, val in enumerate(input_data):
        if i % 2 == 0:
            blocks.append((file_counter, int(val)))
            file_counter += 1
        elif i % 2 == 1:
            blocks.append((None, int(val)))
    return blocks, 0, len(blocks) - 1


def run(input_data: list[str]):
    blocks, start, end = read_data(input_data)
    result = 0
    counter = 0
    visual_result = ''
    while start < len(blocks):
        if not start < end:
            if blocks[start][0] is not None:
                while blocks[start][1] != 0:
                    result += counter * blocks[start][0]
                    visual_result += str(blocks[start][0])
                    counter += 1
                    blocks[start] = ((blocks[start][0]), blocks[start][1] - 1)
                start += 1
            else:
                start += 1
        elif blocks[end][0] is None or blocks[end][1] == 0:
            end -= 1
        elif blocks[start][0] is not None:
            while blocks[start][1] != 0:
                result += counter * blocks[start][0]
                visual_result += str(blocks[start][0])
                counter += 1
                blocks[start] = ((blocks[start][0]), blocks[start][1] - 1)
            start += 1
        elif blocks[start][1] == 0:
            start += 1
        else:
            result += counter * blocks[end][0]
            visual_result += str(blocks[end][0])
            counter += 1
            blocks[start] = ((blocks[start][0]), blocks[start][1] - 1)
            blocks[end] = ((blocks[end][0]), blocks[end][1] - 1)

    return result


if __name__ == '__main__':
    print(run(open('../../data/days/09/data', 'r').readlines()))
