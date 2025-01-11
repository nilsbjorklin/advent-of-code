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


def run(input_data, iterations):
    data = read_data(input_data)
    result = 0
    for number in data:
        for _ in range(iterations):
            number = transform_secret(number)
        result += number
    return result


if __name__ == "__main__":
    print(run(open("src/2024/data/days/22/data", "r").read(), iterations=2000))
