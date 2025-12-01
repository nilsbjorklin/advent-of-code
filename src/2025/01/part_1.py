def run(input_data: list[str]) -> int:
    position = 50
    result = 0
        
    for line in input_data:
        move = parse_line(line.strip())
        position = (position + move) % 100
        print(f"Current position: {position}")
        if position == 0:
            result += 1
    return result

def parse_line(line: str) -> int:
    return int(line[1:]) if line.startswith('L') else -int(line[1:])

if __name__ == "__main__":
    file = open("src/2025/01/data", "r")
    lines = file.readlines()
    print(run(lines))