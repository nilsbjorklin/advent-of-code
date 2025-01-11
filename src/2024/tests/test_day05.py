from importlib import import_module
from unittest import TestCase

part_1 = import_module("src.2024.days.05.part_1")
part_2 = import_module("src.2024.days.05.part_2")

test_data = """
47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47
"""


class TestPart1(TestCase):
    def test_part_1(self):
        self.assertEqual(143, part_1.run(test_data.strip().splitlines()))


class TestPart2(TestCase):

    def test_part_2(self):
        self.assertEqual(123, part_2.run(test_data.strip().splitlines()))
