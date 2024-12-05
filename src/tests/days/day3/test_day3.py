from unittest import TestCase

from src.days.day3.script import Day3


class Part1Test(TestCase):

    def setUp(self):
        self.part1 = Day3.part_1(["xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"])

    def test_part1(self):
        self.assertEqual(161, self.part1.run())


class Part2Test(TestCase):

    def setUp(self):
        self.part2 = Day3.part_2(["xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"])

    def test_part1(self):
        self.assertEqual(48, self.part2.run())
