from collections import deque

def run(input_data):
    chars = deque(input_data)
    last_14 = deque(maxlen=14)
    for index in range(len(chars)):
        if len(last_14) == 14 and len(set(last_14)) == 14:
            return index
        char = chars.popleft()
        last_14.append(char)
    return 0


if __name__ == "__main__":
    print(run(open("src/2022/data/days/06/data", "r").read()))
