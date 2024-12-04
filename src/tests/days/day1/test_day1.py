from unittest import TestCase

from src.days.day1.script import Day1


class Test(TestCase):
    def setUp(self):
        self.day1 = Day1(([1, 2, 2, 1], [3, 5, 6, 1]))

    def test_data_is_sorted(self):
        with self.subTest("list1"):
            self.assertTrue(is_sorted(self.day1.data[0]))
        with self.subTest("list2"):
            self.assertTrue(is_sorted(self.day1.data[1]))

    def test_run(self):
        self.assertEqual(9, self.day1.run())


def is_sorted(lst):
    return all(
        lst[index] <= lst[index + 1]
        for index in range(len(lst) - 1)
    )
