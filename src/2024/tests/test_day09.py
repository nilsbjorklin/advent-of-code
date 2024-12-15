from importlib import import_module
from unittest import TestCase

part_1 = import_module('src.2024.days.day09.part_1')
part_2 = import_module('src.2024.days.day09.part_2')

test_data_mini = '''
12345
'''
test_data = '''
2333133121414131402
'''


class Test(TestCase):

    def test_part_1_mini(self):
        self.assertEqual(60, part_1.run(test_data_mini.strip().splitlines()))

    def test_part_1(self):
        self.assertEqual(1928, part_1.run(test_data.strip().splitlines()))

    def test_part_2(self):
        self.assertEqual(2858, part_2.run(test_data.strip().splitlines()))
