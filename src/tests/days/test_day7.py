from unittest import TestCase

from src.days.day_7 import Day7

data = [
    "190: 10 19",
    "3267: 81 40 27",
    "83: 17 5",
    "156: 15 6",
    "7290: 6 8 6 15",
    "161011: 16 10 13",
    "192: 17 8 14",
    "21037: 9 7 18 13",
    "292: 11 6 16 20"
]


class Part1Test(TestCase):

    def setUp(self):
        self.part1 = Day7.part_1(data)

    def test_part1(self):
        self.assertEqual(3749, self.part1.run())


class Part2Test(TestCase):

    def setUp(self):
        self.part2 = Day7.part_2(data)
