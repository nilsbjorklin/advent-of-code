from collections import defaultdict
from importlib import import_module
from unittest import TestCase

part_1 = import_module('src.2024.days.10.part_1')
part_2 = import_module('src.2024.days.10.part_2')

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


class TestPart1(TestCase):
    def setUp(self):
        part_1.data = []
        part_1.width = part_1.height = 0

    def test_part_1_mini(self):
        self.assertEqual(1, part_1.run(test_data_part_1_mini.strip().splitlines()))

    def test_part_1(self):
        self.assertEqual(36, part_1.run(test_data.strip().splitlines()))

class TestPart2(TestCase):
    def setUp(self):
        part_2.data_array = []
        part_2.width = part_1.height = 0
        part_2.data = defaultdict(set)
        part_2.paths = defaultdict(list)

    def test_part_2_mini(self):
        self.assertEqual(227, part_2.run(test_data_part_2_mini.strip().splitlines()))

    def test_part_2_mini_2(self):
        self.assertEqual(3, part_2.run(test_data_part_2_mini_2.strip().splitlines()))

    def test_part_2_mini_3(self):
        self.assertEqual(13, part_2.run(test_data_part_2_mini_3.strip().splitlines()))

    def test_part_2(self):
        self.assertEqual(81, part_2.run(test_data.strip().splitlines()))
