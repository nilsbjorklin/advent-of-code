from collections import deque


def read_data(input_data: str) -> list:
    return [
        tuple(map(int, player.splitlines()[1:])) for player in input_data.split("\n\n")
    ]


def run(input_data: str) -> int:
    winning_deck, _ = run_game(*read_data(input_data))
    return sum((index + 1) * card for index, card in enumerate(reversed(winning_deck)))


def run_game(deck1, deck2):
    deck1 = deque(deck1)
    deck2 = deque(deck2)
    previous_decks = set()
    while deck1 and deck2:
        if (tuple(deck1), tuple(deck2)) in previous_decks:
            return deck1, True
        previous_decks.add((tuple(deck1), tuple(deck2)))

        card1, card2 = deck1.popleft(), deck2.popleft()

        if card1 <= len(deck1) and card2 <= len(deck2):
            if run_game(tuple(deck1)[:card1], tuple(deck2)[:card2])[1]:
                deck1.extend((card1, card2))
            else:
                deck2.extend((card2, card1))
        else:
            if card1 > card2:
                deck1.extend((card1, card2))
            else:
                deck2.extend((card2, card1))
    return deck1 if deck1 else deck2, bool(deck1)


if __name__ == "__main__":
    print(run(open("data", "r").read()))
