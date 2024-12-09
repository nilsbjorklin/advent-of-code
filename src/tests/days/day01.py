from unittest import TestCase

from src.days.day01.part_1 import run as part_1_run
from src.days.day01.part_2 import run as part_2_run

test_data = '''
03   04
04   03
02   05
01   03
03   9
03   03
'''


class Test(TestCase):

    def test_part_1(self):
        self.assertEqual(11, part_1_run(test_data.strip().splitlines()))

    def test_part_2(self):
        self.assertEqual(31, part_2_run(test_data.strip().splitlines()))
