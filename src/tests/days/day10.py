from unittest import TestCase

from src.days.day10.part_1 import run as part_1_run
from src.days.day10.part_2 import run as part_2_run

test_data_part_1_mini = '''
0123
1234
8765
9876
'''

test_data_part_2_mini = '''
012345
123456
234567
345678
416789
567891
'''

test_data = '''
89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732
'''

test_data_part_2_mini_2 = '''
.....0.
..4321.
..5..2.
..6543.
..7..4.
..8765.
..9....
'''
test_data_part_2_mini_3 = '''
..90..9
...1.98
...2..7
6543456
765.987
876....
987....'''


class Test(TestCase):

    def test_part_1_mini(self):
        self.assertEqual(1, part_1_run(test_data_part_1_mini.strip().splitlines()))

    def test_part_1(self):
        self.assertEqual(36, part_1_run(test_data.strip().splitlines()))

    def test_part_2_mini(self):
        self.assertEqual(227, part_2_run(test_data_part_2_mini.strip().splitlines()))

    def test_part_2_mini_2(self):
        self.assertEqual(3, part_2_run(test_data_part_2_mini_2.strip().splitlines()))

    def test_part_2_mini_3(self):
        self.assertEqual(13, part_2_run(test_data_part_2_mini_3.strip().splitlines()))

    def test_part_2(self):
        self.assertEqual(81, part_2_run(test_data.strip().splitlines()))
