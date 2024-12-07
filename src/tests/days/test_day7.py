from unittest import TestCase

from src.days.day_7 import Day7

data = [
]


class Part1Test(TestCase):

    def setUp(self):
        self.part1 = Day7.part_1(data)


class Part2Test(TestCase):

    def setUp(self):
        self.part2 = Day7.part_2(data)
