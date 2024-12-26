from importlib import import_module

part_1 = import_module("src.2024.days.20.part_1")

test_data = """
###############
#...#...#.....#
#.#.#.#.#.###.#
#S#...#.#.#...#
#######.#.#.###
#######.#.#...#
#######.#.###.#
###..E#...#...#
###.#######.###
#...###...#...#
#.#####.#.###.#
#.#...#.#.#...#
#.#.#.#.#.#.###
#...#...#...###
###############"""


def test_part_1():
    assert part_1.run(test_data, threshold=20) == 5


def test_part_1_no_threshold():
    assert part_1.run(test_data) == 14 + 14 + 2 + 4 + 2 + 3 + 1 + 1 + 1 + 1 + 1
