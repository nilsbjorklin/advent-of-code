from importlib import import_module

part_1 = import_module("src.2024.days.22.part_1")
part_2 = import_module("src.2024.days.22.part_2")


def test_part_1():
    data = """
    1
    10
    100
    2024
    """

    assert part_1.run(data, 2000) == sum([8685429, 4700978, 15273692, 8667524])


def test_part_1_mix():
    assert part_1.mix(15, 42) == 37


def test_part_1_prune():
    assert part_1.prune(100000000) == 16113920


def test_part_1_secret():
    result = []
    value = 123
    for _ in range(10):
        new_value = part_1.transform_secret(value)
        result.append(new_value)
        value = new_value
    assert result == [
        15887950,
        16495136,
        527345,
        704524,
        1553684,
        12683156,
        11100544,
        12249484,
        7753432,
        5908254,
    ]


def test_part_1_transform_secret():
    numbers = [1, 10, 100, 2024]

    for _ in range(2000):
        for i in range(len(numbers)):
            numbers[i] = part_1.transform_secret(numbers[i])

    assert numbers == [8685429, 4700978, 15273692, 8667524]


def test_part_1_price_diff():
    result = []
    value = 123
    price = 3
    for _ in range(10):
        res = part_2.price_diff(value, price)
        value, price, _ = res
        result.append(res)
        print(res)
    assert result == [
        (15887950, 0, -3),
        (16495136, 6, 6),
        (527345, 5, -1),
        (704524, 4, -1),
        (1553684, 4, 0),
        (12683156, 6, 2),
        (11100544, 4, -2),
        (12249484, 4, 0),
        (7753432, 2, -2),
        (5908254, 4, 2),
    ]


def test_part_2_buy():
    data = [1, 2, 3, 2024]
    assert [
        part_2.buy(secret_number, [-2, 1, -1, 3], 2000) for secret_number in data
    ] == [7, 7, None, 9]


def test_part_2():
    data = """
    1
    2
    3
    2024
    """

    assert part_2.run(data, 2000) == [-2, 1, -1, 3]
