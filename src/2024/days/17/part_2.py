import re

registers = [0, 0, 0]
instruction_pointer = 0
output = -1


def read_data(input_data: str) -> list:
    program = re.compile(r"Program: ([\d,]+)").findall(input_data)[0].split(",")
    return list(map(int, program))


def run(input_data):
    program = read_data(input_data)
    return find_lowest_a_value(program, len(program) - 1, 0)


def find_lowest_a_value(program, program_index, a_value):
    global registers
    global output
    global instruction_pointer
    if program_index < 0:
        return a_value
    registers[1] = registers[2] = 0
    for number in range(8):
        registers[0] = a_value << 3 | number
        instruction_pointer = 0
        output = -1
        while instruction_pointer < len(program):
            operand = program[instruction_pointer + 1]
            op_code = program[instruction_pointer]
            if run_operation(op_code, operand):
                break
            instruction_pointer += 2
        if output == program[program_index]:
            next_result = find_lowest_a_value(
                program, program_index - 1, a_value * 8 | number
            )
            if next_result:
                return next_result
    return False


def run_operation(op_code, operand):
    global registers
    global instruction_pointer
    global output
    if op_code == 0:
        registers[0] >>= combo_operand(operand)
    elif op_code == 1:
        registers[1] ^= operand
    elif op_code == 2:
        registers[1] = combo_operand(operand) % 8
    elif op_code == 3:
        if registers[0] != 0:
            instruction_pointer = operand - 2
    elif op_code == 4:
        registers[1] ^= registers[2]
    elif op_code == 5:
        output = combo_operand(operand) % 8
        return True
    elif op_code == 7:
        registers[2] = registers[0] >> combo_operand(operand)
    return False


def combo_operand(operand):
    global registers
    if operand > 3:
        return registers[operand - 4]
    return operand


if __name__ == "__main__":
    print(run(open("src/2024/data/days/17/data", "r").read()))
