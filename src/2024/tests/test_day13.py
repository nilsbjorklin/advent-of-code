from importlib import import_module
from unittest import TestCase

part_1 = import_module('src.2024.days.day13.part_1')
part_2 = import_module('src.2024.days.day13.part_2')

test_data_mini = '''
Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=8400, Y=5400
'''

test_data = '''
Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=8400, Y=5400

Button A: X+26, Y+66
Button B: X+67, Y+21
Prize: X=12748, Y=12176

Button A: X+17, Y+86
Button B: X+84, Y+37
Prize: X=7870, Y=6450

Button A: X+69, Y+23
Button B: X+27, Y+71
Prize: X=18641, Y=10279
'''

class TestPart1(TestCase):
    def test_part_1_mini_1(self):
        self.assertEqual(280, part_1.run(test_data_mini))

    def test_part_1(self):
        self.assertEqual(480, part_1.run(test_data))


class TestPart2(TestCase):

    def test_part_1(self):
        self.assertEqual(875318608908, part_2.run(test_data))
