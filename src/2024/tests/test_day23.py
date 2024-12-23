from importlib import import_module

part_1 = import_module("src.2024.days.23.part_1")
part_2 = import_module("src.2024.days.23.part_2")

test_data_part_1 = """
kh-tc
qp-kh
de-cg
ka-co
yn-aq
qp-ub
cg-tb
vc-aq
tb-ka
wh-tc
yn-cg
kh-ub
ta-co
de-co
tc-td
tb-wq
wh-td
ta-ka
td-qp
aq-cg
wq-ub
ub-vc
de-ta
wq-aq
wq-vc
wh-yn
ka-de
kh-ta
co-tc
wh-qp
tb-vc
td-yn"""

test_data_part_2 = """
ka-co
ta-co
de-co
ta-ka
de-ta
ka-de"""


def test_part_1():
    assert part_1.run(test_data_part_1) == 7


def test_part_2():
    assert part_2.run(test_data_part_2) == "co,de,ka,ta"
