import math

from src.days.functions import time_method


def read_data(input_data):
    stones = []
    for stone in input_data[0].split(' '):
        stones.append(int(stone))
    return stones


def run(input_data: list[str], num_blinks):
    stones = read_data(input_data)
    result = 0
    print(stones, num_blinks)
    for stone in stones:
        result += blink(stone, num_blinks)
    return result


def blink(stone, num_blinks):
    if num_blinks == 0:
        return 1
    elif stone == 0:
        return blink(1, num_blinks - 1)
    num_len = int(math.log10(stone)) + 1
    if num_len % 2 == 0:
        num1, num2 = divmod(stone, 10 ** int(num_len / 2))
        return blink(num1, num_blinks - 1) + blink(num2, num_blinks - 1)
    else:
        return blink(stone * 2024, num_blinks - 1)


if __name__ == '__main__':
    print(time_method('main', run, open('../../data/days/11/data', 'r').readlines(), 25))
