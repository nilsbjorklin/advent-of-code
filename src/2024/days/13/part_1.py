import re


def read_data(input_data):
    data = []
    pattern = re.compile(r"(A|B|Prize): X[+=](\d+), Y[+=](\d+)")
    blank_line_regex = r"(?:\r?\n){2,}"

    for segment in re.split(blank_line_regex, input_data.strip()):
        result = []
        for match in pattern.finditer(segment):
            result.append(int(match.groups()[1]) + int(match.groups()[2]) * 1j)
        data.append(tuple(result))
    return data


def find_solution(machine):
    a, b, prize = machine
    b_amount = 100
    while b_amount >= 0:
        b_value = b * b_amount
        difference = prize - b_value
        if difference.real >= 0 and difference.imag >= 0:
            divisibility = (
                difference.imag / a.imag
                if difference.imag / a.imag == difference.real / a.real
                else None
            )
            if divisibility:
                return int(divisibility * 3) + b_amount
        b_amount -= 1
    return 0


def run(input_data):
    machines = read_data(input_data)
    return sum([find_solution(machine) for machine in machines])


if __name__ == "__main__":
    print(run(open("src/2024/data/days/13/data", "r").read()))
