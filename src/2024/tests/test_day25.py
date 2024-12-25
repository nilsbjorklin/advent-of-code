from importlib import import_module


part_1 = import_module("src.2024.days.25.part_1")


test_data = """
#####
.####
.####
.####
.#.#.
.#...
.....

#####
##.##
.#.##
...##
...#.
...#.
.....

.....
#....
#....
#...#
#.#.#
#.###
#####

.....
.....
#.#..
###..
###.#
###.#
#####

.....
.....
.....
#....
#.#..
#.#.#
#####"""


def test_part_1():
    assert part_1.run(test_data) == 3
