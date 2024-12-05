from unittest import TestCase

from src.days.day_4 import Day4

data = [
    "MMMSXXMASM",
    "MSAMXMSMSA",
    "AMXSXMAAMM",
    "MSAMASMSMX",
    "XMASAMXAMM",
    "XXAMMXXAMA",
    "SMSMSASXSS",
    "SAXAMASAAA",
    "MAMMMXMMMM",
    "MXMXAXMASX"
]


class Part1Test(TestCase):

    def setUp(self):
        self.part1 = Day4.part_1(data)

    def test_part1(self):
        self.assertEqual(18, self.part1.run())


class Part2Test(TestCase):

    def setUp(self):
        self.part2 = Day4.part_2(data)

    def test_part1(self):
        self.assertEqual(9, self.part2.run())
