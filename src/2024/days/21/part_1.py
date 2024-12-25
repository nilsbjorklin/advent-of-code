from collections import defaultdict
from copy import deepcopy
import itertools
import networkx as nx

NUMERICAL_COORDINATES = {
    "7": 0,
    "8": 1,
    "9": 2,
    "4": 1j,
    "5": 1 + 1j,
    "6": 2 + 1j,
    "1": 2j,
    "2": 1 + 2j,
    "3": 2 + 2j,
    "0": 1 + 3j,
    "A": 2 + 3j,
}

DIRECTION_POSITIONS = {"^": 1, "A": 2, "<": 0 + 1j, "v": 1 + 1j, ">": 2 + 1j}
DIRECTION_VALUES = {"A": 0, "^": -1j, "<": -1, "v": 1j, ">": 1}
DIRECTION_CHANGE = {
    key_out: {
        key_in: pos_out - pos_in for key_in, pos_in in DIRECTION_POSITIONS.items()
    }
    for key_out, pos_out in DIRECTION_POSITIONS.items()
}
DIRECTION_WEIGHT = {
    key_out: {
        key_in: abs(pos_out.real - pos_in.real) + abs(pos_out.imag - pos_in.imag)
        for key_in, pos_in in DIRECTION_POSITIONS.items()
    }
    for key_out, pos_out in DIRECTION_POSITIONS.items()
}

directional_graph = nx.Graph()
directional_graph_2 = nx.Graph()

directions = defaultdict(int)


def graph_direction(moves: dict[int] = None, count=0):
    if count > 6:
        new_moves = defaultdict(int)
        for chars, value in moves.items():
            last_char = chars[-1]
            if last_char == "A":
                new_moves[chars] = value
        return new_moves
    elif moves:
        for chars in list(moves.keys()):
            last_pos, weight = moves[chars]
            last_char = chars[-1]
            if last_char != "A":
                for char in DIRECTION_POSITIONS.keys():
                    if char not in chars or char == last_char:
                        moves = add_move(
                            moves=moves,
                            key=chars + char,
                            next_pos=last_pos + DIRECTION_VALUES[char],
                            weight=weight + DIRECTION_WEIGHT[last_char][char],
                        )
    else:
        last_char = "A"
        moves = defaultdict(int)
        for char in DIRECTION_POSITIONS.keys():
            moves = add_move(
                moves=moves,
                key=char,
                next_pos=DIRECTION_VALUES[char],
                weight=DIRECTION_WEIGHT[last_char][char],
            )

    return graph_direction(moves, count + 1)


def best_move(pos_change, depth=0, limit=1):
    if depth > limit:
        return None
    if pos_change == 0:
        return ["A"]

    moves = []
    moves.append("v" * int(pos_change.imag))
    moves.append("^" * int(-pos_change.imag))
    moves.append(">" * int(pos_change.real))
    moves.append("<" * int(-pos_change.real))
    moves = list(filter(bool, moves))

    if depth == limit:
        return moves + ['A']
    new_moves = []
    for permutation in itertools.permutations(moves, len(moves)):
        last_move = "A"
        permutation = list(permutation) + ["A"]
        print(depth, "permutation", permutation)
        perm = []
        for move in permutation:
            for char in move:
                print(depth, "permutation-move", move)
                rec_moves = best_move(
                    DIRECTION_CHANGE[char][last_move], depth=depth + 1, limit=limit
                )
                print(depth, "permutation-rec_moves", rec_moves)
                perm += rec_moves
                last_move = char
        if not new_moves or len(perm) < len(new_moves):
            print(depth, "replacing: ", new_moves, "with: ", perm)
            new_moves = perm
    return new_moves


def add_move(moves, key, next_pos, weight):
    if -2 <= next_pos.real <= 0:
        if -3 <= next_pos.imag <= 1:
            moves[key] = (next_pos, weight)
    return moves


def read_data(input_data: str):
    dir_weights = graph_direction()
    """for moves, value in dir_weights.items():
        pos, weight = value
        print(moves, pos, weight)

    print("CHANGE")
    for k, v_dict in DIRECTION_CHANGE.items():
        for k2, v in v_dict.items():
            print(k, k2, v)
    print("WEIGHTS")
    for k, v_dict in DIRECTION_WEIGHT.items():
        for k2, v in v_dict.items():
            print(k, k2, v)

    best_paths = defaultdict(tuple[str, int])

    for moves, value in dir_weights.items():
        pos, weight = value
        if pos not in best_paths or best_paths[pos][1] > weight:
            best_paths[pos] = (moves, weight)
    print("----------------------------------------")
    for i in range(-2, 1):
        for j in range(-3, 2):
            pos = i + j * 1j
            if pos in best_paths:
                moves, weight = best_paths[pos]
                print(f"{pos}: {weight}: {moves}")
            else:
                print(f"{pos=} not found")
    print("----------------------------------------")
    result_path = ""
    result_value = 0
    prev_pos = NUMERICAL_COORDINATES["A"]
    for pos in [NUMERICAL_COORDINATES[char] for char in "029A"]:
        print(pos)
        if pos in best_paths:
            change = prev_pos - pos
            moves, weight = best_paths[change]
            print((prev_pos, pos), change, moves, weight)
            result_path += moves
            result_value += weight
        prev_pos = pos

    print(result_path, result_value)
    """
    return [line.strip() for line in input_data.splitlines()]


def run(input_data: str) -> int:
    lines = read_data(input_data)
    print()
    print("run 1: ")
    
    print(
        best_move(NUMERICAL_COORDINATES["0"] - NUMERICAL_COORDINATES["A"], limit=1),
    )
    """print("run 0: ")
    print(
        best_move(NUMERICAL_COORDINATES["0"] - NUMERICAL_COORDINATES["A"], limit=0),
    )
    print("run 2: ")
    print(
        best_move(NUMERICAL_COORDINATES["0"] - NUMERICAL_COORDINATES["A"], limit=2),
    )"""
    """for char in lines[0]:
        print("\n", char)
        print(
            best_move(NUMERICAL_COORDINATES[char] - NUMERICAL_COORDINATES["A"], limit=2)
        )
    print(best_move(-2 - 1j))  # A -> 1
    """
    # print(numerical_path(lines[0]))


if __name__ == "__main__":
    print(run(open("src/2024/data/days/21/data", "r").read()))
