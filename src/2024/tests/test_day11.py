from importlib import import_module
from unittest import TestCase

part_1 = import_module('src.2024.days.day11.part_1')
part_2 = import_module('src.2024.days.day11.part_2')


class Test(TestCase):
    def test_part_1_mini(self):
        self.assertEqual(7, part_1.run(['0 1 10 99 999'], 1))

    def test_part_1_steps(self):
        results = [3, 4, 5, 9, 13, 22]
        for i, result in enumerate(results):
            with self.subTest(f'step {i + 1}'):
                self.assertEqual(results[i], part_1.run(['125 17'], i + 1))

    def test_part_1(self):
        self.assertEqual(55312, part_1.run(['125 17'], 25))

    def test_part_2(self):
        self.assertEqual(55312, part_2.run(['125 17'], 25))
