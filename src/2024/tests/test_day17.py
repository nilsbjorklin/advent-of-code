from importlib import import_module
from unittest import TestCase

part_1 = import_module('src.2024.days.17.part_1')
part_2 = import_module('src.2024.days.17.part_2')

test_data_part_1 = '''
Register A: 729
Register B: 0
Register C: 0

Program: 0,1,5,4,3,0'''

test_data_part_2 = '''
Register A: 2024
Register B: 0
Register C: 0

Program: 0,3,5,4,3,0'''


class TestPart1(TestCase):
    def setUp(self):
        part_1.registers = {
            'A': 0,
            'B': 0,
            'C': 0
        }
        part_1.instruction_pointer = 0
        part_1.output = []

    def test_part_1(self):
        self.assertEqual('4,6,3,5,6,3,5,2,1,0', part_1.run(test_data_part_1))

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


class TestPart2(TestCase):
    def setUp(self):
        part_1.registers = {
            'A': 0,
            'B': 0,
            'C': 0
        }
        part_1.instruction_pointer = 0
        part_1.output = []

    def test_part_2(self):
        new_register_a_value = part_2.run(test_data_part_2)
        with self.subTest('part_2 returns expected value'):
            self.assertEqual(117440, new_register_a_value)
        with self.subTest('value validated'):
            part_1.registers['A'] = new_register_a_value
            part_1.run_program(0, 3, 5, 4, 3, 0)
            self.assertEqual('0,3,5,4,3,0', ','.join(map(str, part_1.output)))
