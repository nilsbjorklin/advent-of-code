from importlib import import_module

part_1 = import_module("src.2024.days.20.part_1")
part_2 = import_module("src.2024.days.20.part_2")

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
    
def test_part_2():
    assert part_2.run(test_data, 20, 50) == 32+31+29+39+25+23+20+19+12+14+12+22+4+3
