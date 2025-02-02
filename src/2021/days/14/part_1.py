def read_data(input_data):
    template, insertions = input_data.split("\n\n")
    insertions = [insertion.split("->") for insertion in insertions.splitlines()]
    insertions = {tuple(pattern.strip()): char.split()[0] for pattern, char in insertions}
    return template, insertions


def run(input_data):
    template, insertions = read_data(input_data)
    for _ in range(10):
        new_template = template[0]
        for index in range(len(template) - 1):
            tuple_2 = (template[index], template[index  +1])
            if tuple_2 in insertions.keys():
                new_template += insertions[tuple_2] + template[index + 1]
        template = new_template
        
    least_common = most_common = None
    for char in set(template):
        if least_common is None:
            least_common = most_common = template.count(char)
        else:
            least_common = min(template.count(char), least_common)
            most_common = max(template.count(char), most_common)
    return most_common - least_common

if __name__ == "__main__":
    print(run(open("src/2021/data/days/14/data", "r").read()))
