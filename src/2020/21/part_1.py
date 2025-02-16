from collections import deque


def read_data(input_data: str) -> list:
    return [
        deque(map(int, player.splitlines()[1:])) for player in input_data.split("\n\n")
    ]


def run(input_data: str) -> int:
    deck1, deck2 = read_data(input_data)
    while len(deck1) != 0 and len(deck2) != 0:
        card1, card2 = deck1.popleft(), deck2.popleft()
        if card1 > card2:
            deck1 += [card1, card2]
        else:
            deck2 += [card2, card1]
    return sum(
        (index + 1) * card
        for index, card in enumerate(list(deck1 if len(deck2) == 0 else deck2)[::-1])
    )


if __name__ == "__main__":
    print(run(open("data", "r").read()))
