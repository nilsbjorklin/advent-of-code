import re


def read_data(input_data):
    workflow_data, part_rating_data = input_data.split("\n\n")
    workflows = {}
    for row in workflow_data.splitlines():
        name, rules = re.compile(r"(\w{2,3})\{(.*)\}").findall(row)[0]
        rules = rules.split(",")
        workflows[name] = [
            list(re.compile(r"(\w+)([<>])(\d+):(\w+)").findall(rule)[0])
            for rule in rules[:-1]
        ]
        workflows[name].append(rules[-1:])

    part_ratings = [
        {char: int(value) for char, value in re.compile(r"(\w)=(\d+)").findall(row)}
        for row in part_rating_data.splitlines()
    ]

    return workflows, part_ratings


def run(input_data):
    workflows, part_ratings = read_data(input_data)
    total_result = []
    for part_rating in part_ratings:
        current_flow = "in"
        while current_flow != "A" and current_flow != "R":
            instruction = workflows[current_flow]
            result = run_instruction(part_rating, instruction)
            current_flow = result
        if current_flow == "A":
            total_result.append(sum(part_rating.values()))
    return sum(total_result)


def run_instruction(part_rating, instructions):
    for instruction in instructions:
        if len(instruction) == 1:
            return instruction[0]
        else:
            input_name, condition, condition_limit, output = instruction
            condition_limit = int(condition_limit)
            input_value = part_rating[input_name]
            if input_value > condition_limit if condition == ">" else input_value < condition_limit:
                return output


if __name__ == "__main__":
    print(run(open("src/2023/data/days/19/data", "r").read()))
