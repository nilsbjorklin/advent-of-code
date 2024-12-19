from importlib import import_module
from unittest import TestCase

part_1 = import_module("src.2024.days.03.part_1")
part_2 = import_module("src.2024.days.03.part_2")

test_data = (
    "xmul(02,04)&mul[03,07]!^don't()_mul(05,05)+mul(32,64](mul(11,08)undo()?mul(08,05))"
)


class TestPart1(TestCase):

    def test_part_1(self):
        self.assertEqual(161, part_1.run(test_data.strip().splitlines()))


class TestPart2(TestCase):

    def test_part_2(self):
        self.assertEqual(48, part_2.run(test_data.strip().splitlines()))
