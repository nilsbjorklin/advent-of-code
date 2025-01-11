from importlib import import_module
from unittest import TestCase

part_1 = import_module("src.2024.days.12.part_1")
part_2 = import_module("src.2024.days.12.part_2")

test_data_mini = """
AAAA
BBCD
BBCC
EEEC
"""

test_data_mini_2 = """
OOOOO
OXOXO
OOOOO
OXOXO
OOOOO
"""

test_data_mini_3 = """
EEEEE
EXXXX
EEEEE
EXXXX
EEEEE
"""

test_data_mini_4 = """
AAAAAA
AAABBA
AAABBA
ABBAAA
ABBAAA
AAAAAA
"""

test_data = """
RRRRIICCFF
RRRRIICCCF
VVRRRCCFFF
VVRCCCJFFF
VVVVCJJCFE
VVIVCCJJEE
VVIIICJJEE
MIIIIIJJEE
MIIISIJEEE
MMMISSJEEE
"""


class TestPart1(TestCase):
    def test_part_1_mini_1(self):
        self.assertEqual(140, part_1.run(test_data_mini.strip().splitlines()))

    def test_part_1_mini_2(self):
        self.assertEqual(772, part_1.run(test_data_mini_2.strip().splitlines()))

    def test_part_1(self):
        self.assertEqual(1930, part_1.run(test_data.strip().splitlines()))


class TestPart2(TestCase):
    def test_part_2_mini_1(self):
        self.assertEqual(80, part_2.run(test_data_mini.strip().splitlines()))

    def test_part_2_mini_2(self):
        self.assertEqual(436, part_2.run(test_data_mini_2.strip().splitlines()))

    def test_part_2_mini_3(self):
        self.assertEqual(236, part_2.run(test_data_mini_3.strip().splitlines()))

    def test_part_2_mini_4(self):
        self.assertEqual(368, part_2.run(test_data_mini_4.strip().splitlines()))

    def test_part_2(self):
        self.assertEqual(1206, part_2.run(test_data.strip().splitlines()))
