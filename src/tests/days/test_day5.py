from unittest import TestCase

from src.days.day_5 import Day5

data = [
    "47|53",
    "97|13",
    "97|61",
    "97|47",
    "75|29",
    "61|13",
    "75|53",
    "29|13",
    "97|29",
    "53|29",
    "61|53",
    "97|53",
    "61|29",
    "47|13",
    "75|47",
    "97|75",
    "47|61",
    "75|61",
    "47|29",
    "75|13",
    "53|13",
    "",
    "75,47,61,53,29",
    "97,61,53,29,13",
    "75,29,13",
    "75,97,47,61,53",
    "61,13,29",
    "97,13,75,29,47",
]


class Part1Test(TestCase):

    def setUp(self):
        self.part1 = Day5.part_1(data)

    def test_part1(self):
        self.assertEqual(143, self.part1.run())


class Part2Test(TestCase):

    def setUp(self):
        self.part2 = Day5.part_2(data)

    def test_part2(self):
        self.assertEqual(123, self.part2.run())
