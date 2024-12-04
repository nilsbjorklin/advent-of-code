from unittest import TestCase

from src.days.day2.script import Day2, Part1, Part2


class Part1Test(TestCase):
    data = [[7, 6, 4, 2, 1],
            [1, 2, 7, 8, 9],
            [9, 7, 6, 2, 1],
            [1, 3, 2, 4, 5],
            [8, 6, 4, 4, 1],
            [1, 3, 6, 7, 9]]

    def setUp(self):
        self.part1 = Day2.part_1(self.data)

    def test_part1(self):
        self.assertEqual(2, self.part1.run())

    def test_check_difference(self):
        with self.subTest("plus 4"):
            self.assertTrue(Part1.difference_is_invalid(1, 5))
        with self.subTest("minus 4"):
            self.assertTrue(Part1.difference_is_invalid(5, 1))
        with self.subTest("plus 3"):
            self.assertFalse(Part1.difference_is_invalid(1, 4))
        with self.subTest("minus 3"):
            self.assertFalse(Part1.difference_is_invalid(4, 1))

    def test_check_list(self):
        with self.subTest("ascending valid"):
            self.assertTrue(Part1.list_is_valid([1, 3, 6, 7, 9]))
        with self.subTest("descending valid"):
            self.assertTrue(Part1.list_is_valid([7, 6, 4, 2, 1]))

        with self.subTest("ascending disallowed difference"):
            self.assertFalse(Part1.list_is_valid([1, 2, 7, 8, 9]))
        with self.subTest("descending disallowed difference"):
            self.assertFalse(Part1.list_is_valid([9, 7, 6, 2, 1]))

        with self.subTest("unsorted"):
            self.assertFalse(Part1.list_is_valid([1, 3, 2, 4, 5]))

        with self.subTest("contains equal"):
            self.assertFalse(Part1.list_is_valid([8, 6, 4, 4, 1]))


class Part2Test(TestCase):
    data = [[7, 6, 4, 2, 1],
            [1, 2, 7, 8, 9],
            [9, 7, 6, 2, 1],
            [1, 3, 2, 4, 5],
            [8, 6, 4, 4, 1],
            [1, 3, 6, 7, 9]]

    def setUp(self):
        self.part2 = Day2.part_2(self.data)

    def test_part2(self):
        self.assertEqual(2, self.part2.run())

    def test_sub_array(self):
        self.assertEqual(2, Day2.part_2([[46, 50, 49, 51, 52, 54, 57, 58]]).run())

    def test_check_difference(self):
        with self.subTest("ascending 1"):
            self.assertTrue(Part2.calculate_direction([1, 3, 6, 7, 9]))
        with self.subTest("ascending 2"):
            self.assertTrue(Part2.calculate_direction([1, 2, 7, 8, 9]))
        with self.subTest("ascending 3"):
            self.assertTrue(Part2.calculate_direction([1, 3, 2, 4, 5]))
        with self.subTest("descending 1"):
            self.assertFalse(Part2.calculate_direction([7, 6, 4, 2, 1]))
        with self.subTest("descending 2"):
            self.assertFalse(Part2.calculate_direction([9, 7, 6, 2, 1]))
        with self.subTest("descending 3"):
            self.assertFalse(Part2.calculate_direction([8, 6, 4, 4, 1]))
