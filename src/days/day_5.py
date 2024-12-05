from src.days.template import Template


def parse_data(data):
    parse_rules = True
    rules = {}
    updates = []
    for row in data:
        if len(row.strip()) == 0:
            parse_rules = False
        elif parse_rules:
            before, after = list(map(int, row.split("|")))
            if after in rules:
                rules[after].append(before)
            else:
                rules[after] = [before]
        else:
            updates.append(list(map(int, row.split(","))))
    return rules, updates


class Day5(Template):
    def __init__(self, func, data=0):
        super().__init__(5, func, parse_data, data)

    @staticmethod
    def part_1(data=0):
        return Part1(data)

    @staticmethod
    def part_2(data=0):
        return Part2(data)


class Part1(Day5):
    def __init__(self, data=0):
        super().__init__(self.__func, data)

    def __func(self):
        middle_page_sum = 0
        for update in self.data[1]:
            prev_numbers = []
            update_is_valid = True
            for page in update:
                if not update_is_valid:
                    break
                prev_numbers.append(page)
                if page in self.data[0]:
                    for before in self.data[0][page]:
                        if before not in prev_numbers:
                            if before in update:
                                update_is_valid = False
            if update_is_valid:
                middle_page_sum += update[int(len(update) / 2)]
        return middle_page_sum


class Part2(Day5):
    def __init__(self, data=0):
        super().__init__(self.__func, data)

    def __func(self):
        middle_page_sum = 0
        only_failed_updates = list(filter(self.update_is_faulty, self.data[1]))
        for failed_update in only_failed_updates:
            fixed_update = self.fix_update(failed_update)
            middle_page_sum += fixed_update[int(len(fixed_update) / 2)]
        return middle_page_sum

    def update_is_faulty(self, update):
        prev_numbers = []
        update_is_valid = True
        for page in update:
            prev_numbers.append(page)
            if page in self.data[0]:
                for before in self.data[0][page]:
                    if before not in prev_numbers:
                        if before in update:
                            return True
        return not update_is_valid

    def fix_update(self, update):
        prev_numbers = []
        for page in update:
            prev_numbers.append(page)
            if page in self.data[0]:
                for before in self.data[0][page]:
                    if before not in prev_numbers:
                        if before in update:
                            before_index, after_index = update.index(before), update.index(page)
                            update[after_index], update[before_index] = update[before_index], update[after_index]
                            return self.fix_update(update)
        return update

    def compare(self, item1, item2):
        rules = self.data[0]
        return 1 if (item1 in rules and item2 in rules[item1]) else -1
