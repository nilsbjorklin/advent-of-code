from importlib import import_module
from unittest import TestCase

part_1 = import_module("src.2024.days.04.part_1")
part_2 = import_module("src.2024.days.04.part_2")

test_data = """
MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX
"""


class TestPart1(TestCase):

    def test_part_1(self):
        self.assertEqual(18, part_1.run(test_data.strip().splitlines()))


class TestPart2(TestCase):

    def test_part_2(self):
        self.assertEqual(9, part_2.run(test_data.strip().splitlines()))
