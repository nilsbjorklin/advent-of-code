def read_data(input_data: str) -> list:
    return list(map(int, list(input_data)))


def run(input_data: str, moves) -> str:
    cups = read_data(input_data)
    index = 0
    for move in range(1, moves + 1):
        cup = get_cup(index, cups)
        picked_up_cups = pickup_next_cups(index, cups)
        destination = cup - 1
        while destination in picked_up_cups:
            destination -= 1
        destination = max(cups) if destination < min(cups) else destination
        for picked_up_cup in reversed(picked_up_cups):
            cups.insert(cups.index(destination) + 1, picked_up_cup)
        index = get_cup_index(cups.index(cup) + 1, cups)
    return "".join(
        [
            str(get_cup(index, cups))
            for index in range(cups.index(1) + 1, len(cups) + cups.index(1))
        ]
    )


def get_cup_index(index, cups):
    return index % len(cups)


def get_cup(index, cups):
    return cups[get_cup_index(index, cups)]


def pickup_next_cups(index, cups):
    picked_up_cups = [get_cup(index + i, cups) for i in range(1, 4)]
    for cup in picked_up_cups:
        cups.remove(cup)
    return picked_up_cups


if __name__ == "__main__":
    print(run("394618527", 100))
