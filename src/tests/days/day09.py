from unittest import TestCase

from src.days.day09.part_1 import run as part_1_run
from src.days.day09.part_2 import run as part_2_run

test_data_mini = '''
12345
'''
test_data = '''
2333133121414131402
'''


class Test(TestCase):

    def test_part_1_mini(self):
        self.assertEqual(60, part_1_run(test_data_mini.strip().splitlines()))

    def test_part_1(self):
        self.assertEqual(1928, part_1_run(test_data.strip().splitlines()))

    def test_part_2(self):
        self.assertEqual(2858, part_2_run(test_data.strip().splitlines()))
