from importlib import import_module
from unittest import TestCase

part_1 = import_module('src.2024.days.07.part_1')
part_2 = import_module('src.2024.days.07.part_2')

test_data = '''
190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20
'''


class TestPart1(TestCase):
    def test_part_1(self):
        self.assertEqual(3749, part_1.run(test_data.strip().splitlines()))

class TestPart2(TestCase):

    def test_part_2(self):
        self.assertEqual(11387, part_2.run(test_data.strip().splitlines()))
