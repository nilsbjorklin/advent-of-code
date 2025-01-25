from collections import defaultdict
import re


def read_data(input_data):
    sections = input_data.split("\n\n")
    numbers_map = defaultdict(list)
    numbers_for_boards = defaultdict(lambda: {})
    for board_num, board in enumerate(sections[1:]):
        for y, row in enumerate(board.splitlines()):
            for x, col in enumerate(re.compile("\d+").findall(row)):
                numbers_map[col].append((board_num, complex(x, y)))
                numbers_for_boards[board_num][complex(x, y)] = int(col)
    return sections[0].strip().split(","), numbers_map, numbers_for_boards


def run(input_data: str):
    bingo_numbers, numbers_map, numbers_for_boards = read_data(input_data)
    marked_numbers = defaultdict(set)
    for number in bingo_numbers:
        for board_num, pos in numbers_map[number]:
            marked_numbers[board_num].add(pos)
            numbers_for_boards[board_num][pos] = 0
            if check_for_bingo(marked_numbers[board_num]):
                return sum(numbers_for_boards[board_num].values()) * int(number)


def check_for_bingo(marked_on_board):
    if len(marked_on_board) >= 5:
        for x in range(5):
            if check_row(x, marked_on_board):
                return True
        for y in range(5):
            if check_col(y, marked_on_board):
                return True
    return False


def check_row(x, marked_on_board):
    for y in range(5):
        if complex(x, y) not in marked_on_board:
            return False
    return True


def check_col(y, marked_on_board):
    for x in range(5):
        if complex(x, y) not in marked_on_board:
            return False
    return True


if __name__ == "__main__":
    print(run(open("src/2021/data/days/04/data", "r").read()))
