from importlib import import_module

import pytest

part_1 = import_module("src.2024.days.21.part_1")


def test_part_1():
    data = """029A
980A
179A
456A
379A"""
    assert part_1.run(data) == 126384


def test_part_1_input_to_output_two_layers():
    assert (
        part_1.keypad_output(
            part_1.keypad_output("v<<A>>^A<A>AvA<^AA>A<vAAA>^A", numerical=False)
        )
        == "029A"
    )


def test_part_1_input_to_output_two_layers():
    first_output = part_1.keypad_output(
        "<vA<AA>>^AvAA<^A>A<v<A>>^AvA^A<vA>^A<v<A>^A>AAvA^A<v<A>A>^AAAvA<^A>A",
        numerical=False,
    )
    second_output = part_1.keypad_output(first_output, numerical=False)
    assert (
        part_1.keypad_output(
            "<vA<AA>>^AvAA<^A>A<v<A>>^AvA^A<vA>^A<v<A>^A>AAvA^A<v<A>A>^AAAvA<^A>A",
            numerical=False,
        )
        == "<<vA>>^A<A>AvA<^AA>A<vAAA>^A"
    )
    assert first_output == "v<<A>>^A<A>AvA<^AA>A<vAAA>^A"
    assert second_output == "<A^A>^^AvvvA"
    assert part_1.keypad_output(second_output) == "029A"


def test_part_1_input_to_output():
    assert part_1.keypad_output("<A^A>^^AvvvA") == "029A"
    assert part_1.keypad_output("<A^A^>^AvvvA") == "029A"
    assert part_1.keypad_output("<A^A^^>AvvvA") == "029A"


def test_part_1_output_to_input():
    first_input = part_1.keypad_input("029A")
    second_input = part_1.keypad_input(first_input, numerical=False)
    assert first_input == "<A^A>^^AvvvA"
    assert second_input == "<<vA>>^A<A>AvA<^AA>A<vAAA>^A"
    assert (
        part_1.keypad_input(second_input, numerical=False)
        == "<vA<AA>>^AvAA<^A>A<v<A>>^AvA^A<vA>^A<v<A>^A>AAvA^A<v<A>A>^AAAvA<^A>A"
    )


"""
029A: <vA<AA>>^AvAA<^A>A<v<A>>^AvA^A<vA>^A<v<A>^A>AAvA^A<v<A>A>^AAAvA<^A>A
980A: <v<A>>^AAAvA^A<vA<AA>>^AvAA<^A>A<v<A>A>^AAAvA<^A>A<vA>^A<A>A
179A: <v<A>>^A<vA<A>>^AAvAA<^A>A<v<A>>^AAvA^A<vA>^AA<A>A<v<A>A>^AAAvA<^A>A
456A: <v<A>>^AA<vA<A>>^AAvAA<^A>A<vA>^A<A>A<vA>^A<A>A<v<A>A>^AAvA<^A>A
379A: <v<A>>^AvA^A<vA<AA>>^AAvA<^A>AAvA^A<vA>^AA<A>A<v<A>A>^AAAvA<^A>A
"""
