
def read_data(input_data):
    towel_patterns, design = input_data.split('\n\n')
    [val.strip() for val in towel_patterns.split(',')]
    return [val.strip() for val in towel_patterns.split(',')], design.splitlines()

def create_towel(towel_patterns, design, index=0):
    if index == len(design):
        return True    
    for pattern in towel_patterns:
        if design[index:].startswith(pattern):
            result = create_towel(towel_patterns=towel_patterns, 
                                  design=design, 
                                  index=index + len(pattern))
            if result:
                return True
    return False

def run(input_data):
    towel_patterns, designs = read_data(input_data)
    result = 0
    for design in designs:
        if create_towel(towel_patterns=towel_patterns, design=design):
            print(design)
            result += 1
    return result

if __name__ == '__main__':
    print(run(open('src/2024/days/19/data', 'r').read()))

