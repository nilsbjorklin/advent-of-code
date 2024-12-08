from unittest import TestCase

from src.days.day_8 import Day8

data = [
    "............",
    "........0...",
    ".....0......",
    ".......0....",
    "....0.......",
    "......A.....",
    "............",
    "............",
    "........A...",
    ".........A..",
    "............",
    "............"
]


class Part1Test(TestCase):

    def setUp(self):
        self.part1 = Day8.part_1(data)

    def test_part1(self):
        self.assertEqual(14, self.part1.run())


class Part2Test(TestCase):

    def setUp(self):
        self.part2 = Day8.part_2(data)
