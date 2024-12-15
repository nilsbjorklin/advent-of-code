import re

import numpy as np


def read_data(input_data):
    data = []
    pattern = re.compile(r"(A|B|Prize): X[+=](\d+), Y[+=](\d+)")
    blank_line_regex = r"(?:\r?\n){2,}"

    for segment in re.split(blank_line_regex, input_data.strip()):
        result = []
        for match in pattern.finditer(segment):
            result.append(int(match.groups()[1]))
            result.append(int(match.groups()[2]))
        data.append(np.array(result))
    return data


def find_solution(machine, part1=False):
    a, b, res = np.array_split(machine, 3)
    func_params = np.array(np.rollaxis(np.array([a, b]), 1))
    func_result = res if part1 else np.array(np.add(res, 10000000000000))
    amount = np.linalg.solve(func_params, func_result).round(0).astype(dtype=int)
    return np.sum(np.multiply(amount, [3, 1])) if np.array_equal(func_params @ amount, func_result) else 0


def run(input_data):
    machines = read_data(input_data)
    return sum([find_solution(machine) for machine in machines])


if __name__ == '__main__':
    run(open('../../data/days/13/data', 'r').read())
