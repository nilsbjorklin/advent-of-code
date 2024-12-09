from unittest import TestCase

from src.days.day_6 import Day6

data = [
    "....#.....",
    ".........#",
    "..........",
    "..#.......",
    ".......#..",
    "..........",
    ".#..^.....",
    "........#.",
    "#.........",
    "......#..."
]


class Part1Test(TestCase):

    def setUp(self):
        self.part1 = Day6.part_1(data)

    def test_part1(self):
        self.assertEqual(41, self.part1.run())


class Part2Test(TestCase):

    def setUp(self):
        self.part2 = Day6.part_2(data)

    def test_part2(self):
        self.assertEqual(6, self.part2.run())
