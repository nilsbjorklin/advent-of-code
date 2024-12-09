from unittest import TestCase

from src.days.day04.part_1 import run as part_1_run
from src.days.day04.part_2 import run as part_2_run

test_data = '''
MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX
'''


class Test(TestCase):
    def test_part_1(self):
        self.assertEqual(18, part_1_run(test_data.strip().splitlines()))

    def test_part_2(self):
        self.assertEqual(9, part_2_run(test_data.strip().splitlines()))
