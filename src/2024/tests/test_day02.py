from importlib import import_module
from unittest import TestCase

part_1 = import_module('src.2024.days.02.part_1')
part_2 = import_module('src.2024.days.02.part_2')

test_data = '''
7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9
'''


class TestPart1(TestCase):

    def test_part_1(self):
        self.assertEqual(2, part_1.run(test_data.strip().splitlines()))


class TestPart2(TestCase):

    def test_part_2(self):
        self.assertEqual(4, part_2.run(test_data.strip().splitlines()))
