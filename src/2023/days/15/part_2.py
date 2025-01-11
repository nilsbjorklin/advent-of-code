import re

def read_data(input_data):
    data = []
    pattern = re.compile(r"(\w+)([=-])(\d*)")
    for action in input_data.split(","):
        code, operation, value = pattern.findall(action)[0]
        if operation == '=':
            data.append([code, int(value)])
        else:
            data.append([code])
    return data

def run(input_data):
    rows = read_data(input_data)
    boxes = {}
    for row in rows:
        if len(row) > 1:
            code, value = row
            box = translate_code(code)
            if box not in boxes:
                boxes[box] = {}
            boxes[box][code] = value
        else:
            code = row[0]
            box = translate_code(code)
            if box in boxes and code in boxes[box]:
                del boxes[box][code]
    result = 0
    for box_num, box_items in boxes.items():
        for index, value in enumerate(box_items.values()):
            result += (box_num + 1) * (index + 1) * value
    return result

def translate_code(code):
    result = 0
    for char in code:
        result += ord(char)
        result *= 17
        result = result % 256
    return result
            

if __name__ == "__main__":
    print(run(open("src/2023/data/days/15/data", "r").read()))
