from importlib import import_module
from unittest import TestCase

part_1 = import_module('src.2024.days.18.part_1')
part_2 = import_module('src.2024.days.18.part_2')

test_data = '''
5,4
4,2
4,5
3,0
2,1
6,3
2,4
1,5
0,6
3,3
2,6
5,1
1,2
5,5
2,5
6,5
1,4
0,4
6,4
1,1
6,1
1,0
0,5
1,6
2,0'''


class TestPart1(TestCase):

    def test_part_1(self):
        self.assertEqual(22, part_1.run(test_data, 12, 7))


class TestPart2(TestCase):

    def test_part_2(self):
        self.assertEqual('6,1', part_2.run(test_data, 7))
