from collections import defaultdict
from functools import cmp_to_key
import re

def read_data(input_data):
    maps = []
    pattern = re.compile(r"\d+")
    seeds = []
    for section in input_data.strip().split("\n\n"):
        name = section.split(" ")[0]
        section_map = []
        for row in section.splitlines():
            values = pattern.findall(row)
            if name == "seeds:":
                seeds = list(map(int, values))
            elif values:
                dest, start, reach = list(map(int, values))
                section_map.append((start, start + reach - 1, dest - start))
        if section_map:
            section_map = sorted(section_map, key=cmp_to_key(lambda first, second: first[0] - second[0]))
            maps.append(section_map)
    return seeds, maps

def run(input_data: list[str]):
    seeds, section_mappings = read_data(input_data)
    seed_results = []
    for seed in seeds:
        for section_mapping in section_mappings:
            seed = map_seed(seed, section_mapping)
        seed_results.append(seed)
    return sorted(seed_results)[0]

def map_seed(seed, section_mapping):
    for start, end, change in section_mapping:
        if start > seed:
            return seed
        if start <= seed and end >= seed:
            return seed + change
    return seed

if __name__ == "__main__":
    
    print(run(open("src/2023/data/days/05/data", "r").read()))
