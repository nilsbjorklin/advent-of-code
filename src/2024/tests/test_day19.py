from importlib import import_module

import pytest

part_1 = import_module("src.2024.days.19.part_1")
part_2 = import_module("src.2024.days.19.part_2")

test_data = """
r, wr, b, g, bwu, rb, gb, br

brwrr
bggr
gbbr
rrbgbr
ubwu
bwurrg
brgr
bbrgwb"""


def test_part_1():
    assert part_1.run(test_data) == 6


@pytest.mark.parametrize(
    "input_value,expected",
    [("brwrr", 2), ("bggr", 1), ("gbbr", 4), ("rrbgbr", 6), ("bwurrg", 1), ("brgr", 2)],
)
def test_part_2(input_value, expected):
    test_data = f"r, wr, b, g, bwu, rb, gb, br\n\n{input_value}"
    assert part_2.run(test_data) == expected


def test_part_2_all():
    assert part_2.run(test_data) == 16
