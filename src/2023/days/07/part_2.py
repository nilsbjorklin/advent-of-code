card_strength = ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"][::-1]


def read_data(input_data):
    return [tuple(line.strip().split(" ")) for line in input_data.strip().splitlines()]


def run(input_data: list[str]):
    hands = read_data(input_data)
    hand_dict = {}
    for hand in hands:
        cards, bid = hand
        hand_strength = total_hand_strength(cards)
        hand_dict[hand_strength] = bid

    return sum(
        [
            int(hand_dict[key]) * (index + 1)
            for index, key in enumerate(sorted(hand_dict.keys()))
        ]
    )


def total_hand_strength(cards):
    cards = [hand_type(cards)] + [card_strength.index(card) for card in cards]
    return "".join([chr(card + 97) for card in cards])


def hand_type(cards):
    card_unique = set(cards)
    joker_count = cards.count('J')
    if joker_count:
        card_unique.remove('J')
    counts_len = len(card_unique)
    if counts_len < 2:
        return 6
    elif counts_len == 4:
        return 1
    elif counts_len == 5:
        return 0
    else:
        max_card_count = 0
        for card in card_unique:
            max_card_count = max(max_card_count, cards.count(card) + joker_count)
        if counts_len == 2:
            return 5 if max_card_count == 4 else 4
        elif counts_len == 3:
            return 3 if max_card_count == 3 else 2


if __name__ == "__main__":
    print(run(open("src/2023/data/days/07/data", "r").read()))
