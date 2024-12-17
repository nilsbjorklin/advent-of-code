import re

registers = {
    'A': 0,
    'B': 0,
    'C': 0
}
instruction_pointer = 0
output = []


def read_data(input_data: str) -> [int, int, int, list]:
    global registers
    registers = {k: int(v) for k, v in re.compile(r'Register (\w): (\d+)').findall(input_data)}
    program = re.compile(r'Program: ([\d,]+)').findall(input_data)[0].split(',')
    return list(map(int, program))


def run(input_data):
    program = read_data(input_data)
    run_program(*program)
    return ','.join(map(str, output))


def run_program(*program: int):
    global instruction_pointer
    while instruction_pointer + 1 < len(program):
        op_code = program[instruction_pointer]
        operand = program[instruction_pointer + 1]
        instruction_pointer += 2
        run_operation(op_code, operand)


def run_operation(op_code, operand):
    match op_code:
        case 0:
            adv(combo_operand(operand))
        case 1:
            bxl(operand)
        case 2:
            bst(combo_operand(operand))
        case 3:
            jnz(operand)
        case 4:
            bxc(operand)
        case 5:
            out(combo_operand(operand))
        case 6:
            bvd(combo_operand(operand))
        case 7:
            cvd(combo_operand(operand))
        case _:
            raise ValueError(f'Invalid op_code {op_code}')


def adv(combo):
    global registers
    registers['A'] = registers['A'] // 2 ** combo


def bxl(literal):
    global registers
    registers['B'] = registers['B'] ^ literal


def bst(combo):
    global registers
    registers['B'] = combo % 8


def jnz(literal):
    global instruction_pointer
    if registers['A']:
        instruction_pointer = literal


def bxc(literal):
    global registers
    registers['B'] = registers['B'] ^ registers['C']


def out(combo):
    global output
    output.append(combo % 8)


def bvd(combo):
    registers['B'] = registers['A'] // 2 ** combo


def cvd(combo):
    registers['C'] = registers['A'] // 2 ** combo


def combo_operand(operand):
    match operand:
        case operand if operand < 4:
            return operand
        case 4:
            return registers['A']
        case 5:
            return registers['B']
        case 6:
            return registers['C']
        case _:
            raise ValueError(f'Invalid combo operand {operand}')


if __name__ == '__main__':
    print(run(open('data', 'r').read()))
