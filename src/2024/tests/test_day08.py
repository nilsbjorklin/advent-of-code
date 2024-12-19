from importlib import import_module
from unittest import TestCase

part_1 = import_module('src.2024.days.08.part_1')
part_2 = import_module('src.2024.days.08.part_2')

test_data = '''
............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............
'''


class TestPart1(TestCase):

    def test_part_1(self):
        self.assertEqual(14, part_1.run(test_data.strip().splitlines()))

class TestPart2(TestCase):
    def test_part_2(self):
        self.assertEqual(34, part_2.run(test_data.strip().splitlines()))
