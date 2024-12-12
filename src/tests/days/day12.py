from unittest import TestCase

from src.days.day12.part_1 import run as part_1_run

test_data_mini = '''
AAAA
BBCD
BBCC
EEEC
'''

test_data_mini_2 = '''
OOOOO
OXOXO
OOOOO
OXOXO
OOOOO
'''

test_data = '''
RRRRIICCFF
RRRRIICCCF
VVRRRCCFFF
VVRCCCJFFF
VVVVCJJCFE
VVIVCCJJEE
VVIIICJJEE
MIIIIIJJEE
MIIISIJEEE
MMMISSJEEE
'''


class Test(TestCase):
    def test_part_1_mini_1(self):
        self.assertEqual(140, part_1_run(test_data_mini.strip().splitlines()))

    def test_part_1_mini_2(self):
        self.assertEqual(772, part_1_run(test_data_mini_2.strip().splitlines()))

    def test_part_1(self):
        self.assertEqual(1930, part_1_run(test_data.strip().splitlines()))
