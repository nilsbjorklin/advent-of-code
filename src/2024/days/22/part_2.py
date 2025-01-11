from collections import defaultdict, deque

sequences = defaultdict(lambda: defaultdict(int))


def read_data(input_data):
    return [int(val.strip()) for val in input_data.strip().splitlines()]


def mix(value, secret_number):
    return value ^ secret_number


def prune(secret_number):
    return secret_number % 16777216


def transform_secret(secret_number):
    """
    Calculate the result of multiplying the secret number by 64. Then, mix this result into the secret number. Finally, prune the secret number.
    Calculate the result of dividing the secret number by 32. Round the result down to the nearest integer. Then, mix this result into the secret number. Finally, prune the secret number.
    Calculate the result of multiplying the secret number by 2048. Then, mix this result into the secret number. Finally, prune the secret number.
    """
    secret_number = prune(mix(secret_number, 64 * secret_number))
    secret_number = prune(mix(secret_number, secret_number // 32))
    secret_number = prune(mix(secret_number, 2048 * secret_number))
    return secret_number


def price_diff(secret_number, price):
    new_secret_number = transform_secret(secret_number)
    new_price = new_secret_number % 10
    diff = new_price - price
    return new_secret_number, new_price, diff


def run_sequences(secret_number, iterations, index):
    diff_sequence = deque([], maxlen=4)
    price = secret_number % 10
    for _ in range(iterations):
        diff_res = price_diff(secret_number, price)
        secret_number, price, diff = diff_res
        diff_sequence.append(diff)
        if len(diff_sequence) == 4 and index not in sequences[tuple(diff_sequence)]:
            sequences[tuple(diff_sequence)][index] = price


def run(input_data, iterations):
    data = read_data(input_data)
    for index, secret_number in enumerate(data):
        run_sequences(secret_number, iterations, index)
    max_total = 0
    max_sequence = ()
    for sequence, num_dict in sequences.items():
        total = sum(num_dict.values())
        if total > max_total:
            max_total = total
            max_sequence = sequence
    return list(max_sequence)


if __name__ == "__main__":
    print(run(open("src/2024/data/days/22/data", "r").read(), iterations=2000))
