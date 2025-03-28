from importlib import import_module
from unittest import TestCase

part_1 = import_module("src.2024.days.06.part_1")
part_2 = import_module("src.2024.days.06.part_2")

test_data = """
....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...
"""


class TestPart1(TestCase):
    def test_part_1(self):
        self.assertEqual(41, part_1.run(test_data.strip().splitlines()))


class TestPart2(TestCase):

    def test_part_2(self):
        self.assertEqual(6, part_2.run(test_data.strip().splitlines()))
