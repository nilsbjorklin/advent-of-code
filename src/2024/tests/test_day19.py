from importlib import import_module
from unittest import TestCase

part_1 = import_module('src.2024.days.19.part_1')

test_data = '''
r, wr, b, g, bwu, rb, gb, br

brwrr
bggr
gbbr
rrbgbr
ubwu
bwurrg
brgr
bbrgwb'''


class TestPart1(TestCase):

    def test_part_1(self):
        self.assertEqual(6, part_1.run(test_data))

