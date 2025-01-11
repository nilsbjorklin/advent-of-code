from collections import defaultdict


def read_data(input_data):
    parse_rules = True
    rules = defaultdict(list)
    updates = []
    for row in input_data:
        if len(row.strip()) == 0:
            parse_rules = False
        elif parse_rules:
            before, after = list(map(int, row.split("|")))
            rules[after].append(before)
        else:
            updates.append(list(map(int, row.split(","))))
    return rules, updates


def run(input_data: list[str]):
    rules, updates = read_data(input_data)
    middle_page_sum = 0
    for update in updates:
        prev_numbers = []
        update_is_valid = True
        for page in update:
            if not update_is_valid:
                break
            prev_numbers.append(page)
            if page in rules:
                for before in rules[page]:
                    if before not in prev_numbers:
                        if before in update:
                            update_is_valid = False
        if update_is_valid:
            middle_page_sum += update[int(len(update) / 2)]
    return middle_page_sum


if __name__ == "__main__":
    print(run(open("src/2024/data/days/05/data", "r").readlines()))
