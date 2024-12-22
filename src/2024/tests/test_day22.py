from importlib import import_module

part_1 = import_module("src.2024.days.22.part_1")


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
    for _i in range(10):
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
    """
    1: 8685429
    10: 4700978
    100: 15273692
    2024: 8667524
    """
    numbers = [1, 10, 100, 2024]

    for _ in range(2000):
        for i in range(len(numbers)):
            numbers[i] = part_1.transform_secret(numbers[i])

    assert numbers == [8685429, 4700978, 15273692, 8667524]
