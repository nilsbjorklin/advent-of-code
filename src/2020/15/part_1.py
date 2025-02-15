from collections import defaultdict, deque


def run(input_data: str, limit: int) -> int:
    numbers = list(map(int, input_data.split(",")))
    last_number = numbers[-1]
    last_spoken = defaultdict(lambda: deque(maxlen=2))
    for index, number in enumerate(numbers):
        last_spoken[number].append(index + 1)
    for step in range(len(numbers), limit):
        spoken_at = last_spoken[last_number]
        number = spoken_at[1] - spoken_at[0] if len(spoken_at) == 2 else 0
        last_number = number
        last_spoken[number].append(step + 1)
    return last_number


if __name__ == "__main__":
    print(run("19,20,14,0,9,1", 2020))
