from unittest import TestCase

from src.days.day11.part_1 import run as part_1_run
from src.days.day11.part_2 import run as part_2_run


class Test(TestCase):
    def test_part_1_mini(self):
        self.assertEqual(7, part_1_run(['0 1 10 99 999'], 1))

    def test_part_1_steps(self):
        results = [3, 4, 5, 9, 13, 22]
        for i, result in enumerate(results):
            with self.subTest(f'step {i + 1}'):
                self.assertEqual(results[i], part_1_run(['125 17'], i + 1))

    def test_part_1(self):
        self.assertEqual(55312, part_1_run(['125 17'], 25))

    def test_part_2(self):
        self.assertEqual(55312, part_2_run(['125 17'], 25))
