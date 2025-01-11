from importlib import import_module

part_1 = import_module("src.2024.days.24.part_1")

test_data_part_1_mini = """
x00: 1
x01: 1
x02: 1
y00: 0
y01: 1
y02: 0

x00 AND y00 -> z00
x01 XOR y01 -> z01
x02 OR y02 -> z02"""

test_data_part_1 = """
x00: 1
x01: 0
x02: 1
x03: 1
x04: 0
y00: 1
y01: 1
y02: 1
y03: 1
y04: 1

ntg XOR fgs -> mjb
y02 OR x01 -> tnw
kwq OR kpj -> z05
x00 OR x03 -> fst
tgd XOR rvg -> z01
vdt OR tnw -> bfw
bfw AND frj -> z10
ffh OR nrd -> bqk
y00 AND y03 -> djm
y03 OR y00 -> psh
bqk OR frj -> z08
tnw OR fst -> frj
gnj AND tgd -> z11
bfw XOR mjb -> z00
x03 OR x00 -> vdt
gnj AND wpb -> z02
x04 AND y00 -> kjc
djm OR pbm -> qhw
nrd AND vdt -> hwm
kjc AND fst -> rvg
y04 OR y02 -> fgs
y01 AND x02 -> pbm
ntg OR kjc -> kwq
psh XOR fgs -> tgd
qhw XOR tgd -> z09
pbm OR djm -> kpj
x03 XOR y03 -> ffh
x00 XOR y04 -> ntg
bfw OR bqk -> z06
nrd XOR fgs -> wpb
frj XOR qhw -> z04
bqk OR frj -> z07
y03 OR x01 -> nrd
hwm AND bqk -> z03
tgd XOR rvg -> z12
tnw OR pbm -> gnj"""


def test_part_1_mini():
    assert part_1.run(test_data_part_1_mini) == 4


def test_part_1():
    result = [
        ("bfw", 1),
        ("bqk", 1),
        ("djm", 1),
        ("ffh", 0),
        ("fgs", 1),
        ("frj", 1),
        ("fst", 1),
        ("gnj", 1),
        ("hwm", 1),
        ("kjc", 0),
        ("kpj", 1),
        ("kwq", 0),
        ("mjb", 1),
        ("nrd", 1),
        ("ntg", 0),
        ("pbm", 1),
        ("psh", 1),
        ("qhw", 1),
        ("rvg", 0),
        ("tgd", 0),
        ("tnw", 1),
        ("vdt", 1),
        ("wpb", 0),
        ("z00", 0),
        ("z01", 0),
        ("z02", 0),
        ("z03", 1),
        ("z04", 0),
        ("z05", 1),
        ("z06", 1),
        ("z07", 1),
        ("z08", 1),
        ("z09", 1),
        ("z10", 1),
        ("z11", 0),
        ("z12", 0),
    ]
    assert part_1.run(test_data_part_1) == 2024
    for gate_value in result:
        gate, value = gate_value
        assert part_1.gates[gate] == value
