from collections import defaultdict

rules = defaultdict(list)
updates = []


def read_data(input_data):
    global rules
    global updates
    parse_rules = True
    for row in input_data:
        if len(row.strip()) == 0:
            parse_rules = False
        elif parse_rules:
            before, after = list(map(int, row.split("|")))
            rules[after].append(before)
        else:
            updates.append(list(map(int, row.split(","))))


def run(input_data: list[str]):
    read_data(input_data)
    middle_page_sum = 0
    only_failed_updates = list(filter(update_is_faulty, updates))
    for failed_update in only_failed_updates:
        fixed_update = fix_update(failed_update)
        middle_page_sum += fixed_update[int(len(fixed_update) / 2)]
    return middle_page_sum


def update_is_faulty(all_updates):
    prev_numbers = []
    update_is_valid = True
    for page in all_updates:
        prev_numbers.append(page)
        if page in rules:
            for before in rules[page]:
                if before not in prev_numbers:
                    if before in all_updates:
                        return True
    return not update_is_valid


def fix_update(update):
    prev_numbers = []
    for page in update:
        prev_numbers.append(page)
        if page in rules:
            for before in rules[page]:
                if before not in prev_numbers:
                    if before in update:
                        before_index, after_index = update.index(before), update.index(page)
                        update[after_index], update[before_index] = update[before_index], update[after_index]
                        return fix_update(update)
    return update


if __name__ == '__main__':
    print(run(open('src/2024/data/days/05/data', 'r').readlines()))
