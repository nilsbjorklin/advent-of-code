from importlib import import_module
from unittest import TestCase

part_1 = import_module('src.2024.days.day17.part_1')

test_data = '''
Register A: 729
Register B: 0
Register C: 0

Program: 0,1,5,4,3,0'''


class TestPart1(TestCase):
    def test_part_1(self):
        self.assertEqual('4,6,3,5,6,3,5,2,1,0', part_1.run(test_data))

    def test_part_1_case_1(self):
        part_1.registers['C'] = 9
        part_1.run_program(2, 6)
        self.assertEqual(1, part_1.registers['B'])

    def test_part_1_case_2(self):
        part_1.registers['A'] = 10
        part_1.run_program(5, 0, 5, 1, 5, 4)
        self.assertEqual([0, 1, 2], part_1.output)

    def test_part_1_case_3(self):
        part_1.registers['A'] = 2024
        part_1.run_program(0, 1, 5, 4, 3, 0)
        with self.subTest():
            self.assertEqual([4, 2, 5, 6, 7, 7, 7, 7, 3, 1, 0], part_1.output)
        with self.subTest():
            self.assertEqual(0, part_1.registers['A'])

    def test_part_1_case_4(self):
        part_1.registers['B'] = 29
        part_1.run_program(1, 7)
        self.assertEqual(26, part_1.registers['B'])

    def test_part_1_case_5(self):
        part_1.registers['B'] = 2024
        part_1.registers['C'] = 43690
        part_1.run_program(4, 0)
        self.assertEqual(44354, part_1.registers['B'])
