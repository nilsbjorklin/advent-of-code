seat_values = {"L": False, "#": True}

adjacent = [1, -1, 1j, -1j, 1 + 1j, -1 + 1j, 1 - 1j, -1 - 1j]


def read_data(input_data: str) -> dict:
    seats = {}
    for y, row in enumerate(input_data.splitlines()):
        for x, value in enumerate(row):
            if value in seat_values:
                seats[complex(x, y)] = seat_values[value]
    return seats


def run(input_data: str) -> int:
    seats = read_data(input_data)
    while True:
        seat_changes = []
        for pos in seats.keys():
            value = seats[pos]
            adjacent_filled_seats = 0
            for direction in adjacent:
                adjacent_pos = direction + pos
                if adjacent_pos in seats and seats[adjacent_pos]:
                    adjacent_filled_seats += 1
            if value and adjacent_filled_seats > 3:
                seat_changes.append(pos)
            elif not value and adjacent_filled_seats == 0:
                seat_changes.append(pos)
        if len(seat_changes) == 0:
            return sum(1 for v in seats.values() if v)
        for pos in seat_changes:
            seats[pos] = not seats[pos]


if __name__ == "__main__":
    print(run(open("data", "r").read()))
