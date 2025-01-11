from collections import defaultdict

def read_data(input_data):
    return input_data.strip().splitlines()

def run(input_data):
    rows = read_data(input_data)
    floor = defaultdict(lambda: 0)
    result = 0
    for row_idx, row in enumerate(rows):
        for col_idx, char in enumerate(row):
            if char == '#':
                floor[col_idx] = row_idx + 1                  
            elif char == 'O':                    
                result += len(rows) - floor[col_idx]
                floor[col_idx] += 1
    return result
            

if __name__ == "__main__":    
    print(run(open("src/2023/data/days/14/data", "r").read()))
