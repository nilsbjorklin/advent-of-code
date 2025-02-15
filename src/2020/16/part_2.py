import re
from collections import defaultdict
from functools import lru_cache, reduce

rules = {}


def read_data(input_data: str) -> (list, list):
    global rules
    rules, my_ticket, nearby_tickets = input_data.split("\n\n")
    pattern = re.compile(r"(\d+)-(\d+)")
    rules = {
        name: values
        for name, values in [line.split(":") for line in rules.splitlines()]
    }
    for name, values in rules.items():
        rules[name] = [
            (int(min_value), int(max_value))
            for min_value, max_value in pattern.findall(values)
        ]
    return parse_ticket(my_ticket.splitlines()[1]), [
        parse_ticket(line) for line in nearby_tickets.splitlines()[1:]
    ]


def parse_ticket(line):
    return list(map(int, line.split(",")))


def run(input_data: str) -> int:
    my_ticket, nearby_tickets = read_data(input_data)
    valid_tickets = list(filter(ticket_is_valid, nearby_tickets))
    columns = []
    for value in my_ticket:
        columns.append([value])
    for nearby_ticket in valid_tickets:
        for index, value in enumerate(nearby_ticket):
            columns[index].append(value)
    column_to_rule = {index: fit_rules(column) for index, column in enumerate(columns)}
    rule_to_column = defaultdict(list)
    for column, rule_names in column_to_rule.items():
        for rule_name in rule_names:
            rule_to_column[rule_name].append(column)
    found_rules = []
    while len(column_to_rule.keys()) != 0:
        found_columns = determine_rules(column_to_rule, rule_to_column)
        found_rules += found_columns
        column_to_rule, rule_to_column = trim_rules(
            found_columns, column_to_rule, rule_to_column
        )
    return reduce(
        lambda a, b: a * b,
        [
            my_ticket[column]
            for column, rule_name in found_rules
            if rule_name.startswith("departure")
        ],
        1,
    )


def determine_rules(column_to_rule, rule_to_column):
    found_columns = []
    for column, rules_for_column in column_to_rule.items():
        if len(rules_for_column) == 1:
            found_columns.append((column, rules_for_column[0]))
    for rule, columns_for_rule in rule_to_column.items():
        if len(columns_for_rule) == 1:
            found_columns.append((columns_for_rule[0], rule))
    return found_columns


def trim_rules(found_columns, column_to_rule, rule_to_column):
    for found_column, found_rule in found_columns:
        if found_column in column_to_rule:
            del column_to_rule[found_column]
        if found_rule in rule_to_column:
            del rule_to_column[found_rule]
        for column, rules_for_column in column_to_rule.items():
            if found_rule in rules_for_column:
                rules_for_column.remove(found_rule)
                column_to_rule[column] = rules_for_column
        for rule, columns_for_rule in rule_to_column.items():
            if found_column in columns_for_rule:
                columns_for_rule.remove(found_column)
                rule_to_column[rule] = columns_for_rule
    return column_to_rule, rule_to_column


def fit_rules(column):
    return [rule for rule in rules.keys() if fits_rule(column, rule)]


def fits_rule(column, rule):
    for number in column:
        if not fits_rule_part(number, rule):
            return False
    return True


def fits_rule_part(number, rule):
    for min_value, max_value in rules[rule]:
        if min_value <= number <= max_value:
            return True
    return False


def ticket_is_valid(ticket):
    for number in ticket:
        if not is_valid(number):
            return False
    return True


@lru_cache
def is_valid(number):
    for values in rules.values():
        for min_value, max_value in values:
            if min_value <= number <= max_value:
                return True
    return False


if __name__ == "__main__":
    print(run(open("data", "r").read()))
