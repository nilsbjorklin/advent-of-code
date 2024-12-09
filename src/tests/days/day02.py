from unittest import TestCase

from src.days.day02.part_1 import run as part_1_run
from src.days.day02.part_2 import run as part_2_run

test_data = '''
7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9
'''


class Test(TestCase):
    def test_part_1(self):
        self.assertEqual(2, part_1_run(test_data.strip().splitlines()))

    def test_part_2(self):
        self.assertEqual(4, part_2_run(test_data.strip().splitlines()))
