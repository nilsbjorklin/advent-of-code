from collections import defaultdict


def read_data(input_data):
    fishes = list(map(int, input_data.split(",")))
    return {fish: fishes.count(fish) for fish in set(fishes)}


def run(input_data: str, days):
    fishes = read_data(input_data)
    for _ in range(days):
        fishes = calc_fishes(fishes)
    
    return sum(fishes.values())


def calc_fishes(fishes):
    new_fishes = defaultdict(int)    
    for fish, count in fishes.items():
        if fish == 0:
            new_fishes[8] += count
            new_fishes[6] += count
        else:
            new_fishes[fish-1] += count
    return new_fishes
    

if __name__ == "__main__":
    print(run(open("src/2021/data/days/06/data", "r").read(), 256))
