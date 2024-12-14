from unittest import TestCase

from src.days.day14.part_1 import run as part_1_run
from src.days.day14.part_2 import run as part_2_run

test_data_part_1 = '''
p=0,4 v=3,-3
p=6,3 v=-1,-3
p=10,3 v=-1,2
p=2,0 v=2,-1
p=0,0 v=1,3
p=3,0 v=-2,-2
p=7,6 v=-1,-3
p=3,0 v=-1,-2
p=9,3 v=2,3
p=7,3 v=-1,2
p=2,4 v=2,-3
p=9,5 v=-3,-3
'''

test_data_part_2 = '''
p=0,4 v=3,-3
p=0,3 v=-1,-3
p=0,3 v=-1,2
p=2,0 v=2,-1
p=0,0 v=1,3
p=3,0 v=-2,-2
p=7,6 v=-1,-3
p=3,0 v=-1,-2
p=9,3 v=2,3
p=7,3 v=-1,2
p=2,4 v=2,-3
p=9,5 v=-3,-3
'''


class TestPart1(TestCase):
    def test_part_1_mini_1(self):
        self.assertEqual(12, part_1_run(test_data_part_1.strip().splitlines(), 100, [11, 7]))

    def test_part_2(self):
        part_2_run(test_data_part_2.strip().splitlines(), [11, 7])
