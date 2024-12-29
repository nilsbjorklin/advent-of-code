from importlib import import_module

part_1 = import_module("src.2023.days.01.part_1")

test_data_part_1 = """
1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet
"""


def test_part_1(self):
    assert part_1.run(test_data_part_1.strip().splitlines()) == 142
