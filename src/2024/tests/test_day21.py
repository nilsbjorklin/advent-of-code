from importlib import import_module

part_1 = import_module("src.2024.days.21.part_1")

test_data = """
029A
980A
179A
456A
379A"""


def test_part_1():
    assert part_1.run(test_data, 2) == 126384