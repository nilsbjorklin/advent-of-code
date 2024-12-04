from types import LambdaType
from unittest import TestCase

from src.days.day1.script import Day1


class Test(TestCase):
    def setUp(self):
        self.day1 = Day1(LambdaType, ([1, 2, 2, 1], [3, 5, 6, 1]))
        self.part1 = Day1.part_1(([1, 2, 2, 1], [3, 5, 6, 1]))
        self.part2 = Day1.part_2(([3, 4, 2, 1, 3, 3], [4, 3, 5, 3, 9, 3]))

    def test_data_is_sorted(self):
        with self.subTest("list1"):
            self.assertTrue(is_sorted(self.day1.data[0]))
        with self.subTest("list2"):
            self.assertTrue(is_sorted(self.day1.data[1]))

    def test_part1(self):
        self.assertEqual(9, self.part1.run())

    def test_part2(self):
        self.assertEqual(31, self.part2.run())


def is_sorted(lst):
    return all(
        lst[index] <= lst[index + 1]
        for index in range(len(lst) - 1)
    )
