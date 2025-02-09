from collections import deque


def read_data(input_data: str) -> list[int]:
    return list(map(int, input_data.splitlines()))


def run(input_data: str, last_nums) -> int:
    numbers: list[int] = read_data(input_data)
    invalid_number = find_invalid_number(numbers, last_nums)
    last_numbers = deque()
    index = 0
    while sum(last_numbers) != invalid_number:
        if sum(last_numbers) > invalid_number:
            last_numbers.popleft()
            while sum(last_numbers) > invalid_number:
                last_numbers.pop()
                index -= 1
        else:
            last_numbers.append(numbers[index])
            index += 1
    return min(last_numbers) + max(last_numbers)


def find_invalid_number(numbers, index):
    last_numbers = deque(numbers[:index], maxlen=index)
    for index in range(index, len(numbers)):
        if number_valid(numbers[index], last_numbers):
            last_numbers.append(numbers[index])
        else:
            return numbers[index]


def number_valid(target, last_numbers):
    last_numbers_sorted = sorted(last_numbers)
    for index, first_number in enumerate(last_numbers_sorted):
        if first_number > target:
            return False
        for second_index in range(index + 1, len(last_numbers_sorted)):
            diff = last_numbers_sorted[second_index] + first_number - target
            if diff == 0:
                return True
            elif diff > 0:
                break


if __name__ == "__main__":
    print(run(open("data", "r").read(), 25))
