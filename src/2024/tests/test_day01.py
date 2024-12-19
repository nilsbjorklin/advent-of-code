from importlib import import_module
from unittest import TestCase

part_1 = import_module('src.2024.days.01.part_1')
part_2 = import_module('src.2024.days.01.part_2')

test_data = '''
03   04
04   03
02   05
01   03
03   9
03   03
'''



class TestPart1(TestCase):

    def test_part_1(self):
        self.assertEqual(11, part_1.run(test_data.strip().splitlines()))

class TestPart2(TestCase):
    
    def test_part_2(self):
        self.assertEqual(31, part_2.run(test_data.strip().splitlines()))
