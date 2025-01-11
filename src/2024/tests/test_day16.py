from importlib import import_module
from unittest import TestCase

part_1 = import_module("src.2024.days.16.part_1")
part_2 = import_module("src.2024.days.16.part_2")

test_data_mini = """
###############
#.......#....E#
#.#.###.#.###.#
#.....#.#...#.#
#.###.#####.#.#
#.#.#.......#.#
#.#.#####.###.#
#...........#.#
###.#.#####.#.#
#...#.....#.#.#
#.#.#.###.#.#.#
#.....#...#.#.#
#.###.#.#.#.#.#
#S..#.....#...#
###############"""

test_data = """
#################
#...#...#...#..E#
#.#.#.#.#.#.#.#.#
#.#.#.#...#...#.#
#.#.#.#.###.#.#.#
#...#.#.#.....#.#
#.#.#.#.#.#####.#
#.#...#.#.#.....#
#.#.#####.#.###.#
#.#.#.......#...#
#.#.###.#####.###
#.#.#...#.....#.#
#.#.#.#####.###.#
#.#.#.........#.#
#.#.#.#########.#
#S#.............#
#################
"""


class TestPart1(TestCase):
    def test_part_1_mini(self):
        self.assertEqual(7036, part_1.run(test_data_mini))

    def test_part_1(self):
        self.assertEqual(11048, part_1.run(test_data))


class TestPart2(TestCase):
    def test_part_2_mini(self):
        self.assertEqual(45, part_2.run(test_data_mini))

    def test_part_2(self):
        self.assertEqual(64, part_2.run(test_data))
