from collections import deque

def run(input_data):
    chars = deque(input_data)
    last_4 = deque(maxlen=4)
    for index in range(len(chars)):
        if len(last_4) == 4 and len(set(last_4)) == 4:
            return index
        char = chars.popleft()
        last_4.append(char)
    return 0


if __name__ == "__main__":
    print(run(open("src/2022/data/days/06/data", "r").read()))
