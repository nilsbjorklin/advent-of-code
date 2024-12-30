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
                seed_values = list(map(int, values))
                seeds = [
                    (seed_values[i], seed_values[i] + seed_values[i + 1])
                    for i in range(0, len(seed_values), 2)
                ]
            elif values:
                dest, start, reach = list(map(int, values))
                section_map.append((start, start + reach - 1, dest - start))
        if section_map:
            section_map = sorted(
                section_map, key=cmp_to_key(lambda first, second: first[0] - second[0])
            )
            maps.append(section_map)
    return seeds, maps


def run(input_data: list[str]):
    seeds, section_mappings = read_data(input_data)
    print("start seeds", seeds, "\n")
    for section_mapping in section_mappings:
        seeds = map_seeds(seeds, section_mapping)
        print("SORTED:", sorted(map(lambda x: x[0], seeds)))
    return sorted(map(lambda x: x[0], seeds))[0]

def map_seeds(seeds, section_mapping):
    new_seeds = []
    print_str = ""
    for seed_start, seed_end in seeds:
        seeds_for_seed = []
        for start, end, change in section_mapping:
            print_str = f"input: {(seed_start, seed_end)}:{(start, end)}"
            if start <= seed_start and end >= seed_end:
                seeds_for_seed.append((seed_start + change, seed_end + change))
                print_str += f" > within: change by {change} => {(seed_start + change, seed_end + change)}"
                seed_start = seed_end + 1
                break
            if seed_start <= start <= seed_end:
                    seeds_for_seed.append((start + change, seed_end + change))
                    print_str += f" > start: {seed_start, seed_end}"
                    print_str += f" > split at start {start}: {start, seed_end}"
                    print_str += f" > then change by {change} => {(seed_start + change, seed_end + change)}"
                    seed_end = start - 1
                    print_str += f"updated seed: {(seed_start, seed_end)}"
            elif seed_start <= end <= seed_end:
                seeds_for_seed.append((seed_start + change, end + change))
                print_str += f" > end: {seed_start, seed_end}"
                print_str += f" > split at end {end}: {seed_start, end}"
                print_str += f" > then change by {change} => {(seed_start + change, end + change)}\n"
                seed_start = end + 1
                print_str += f"updated seed: {(seed_start, seed_end)}"
            else:
                print_str += " > outside"
        if seed_start <= seed_end:
            print_str += f" > left: {(seed_start, seed_end)}"
            seeds_for_seed.append((seed_start, seed_end))
        new_seeds += seeds_for_seed
        print(print_str)
    print("result", new_seeds)
    new_seeds = join_seeds(new_seeds)
    print()
    return new_seeds

def join_seeds(seeds):
    seeds = sorted(seeds, key=cmp_to_key(lambda first, second: first[0] - second[0]))
    new_seeds = []
    for index in range(1, len(seeds)):
        start_1, end_1 = seeds[index-1]
        start_2, end_2 = seeds[index]
        if end_1 >= start_2:
            seeds[index] = (start_1, max(end_2, end_1))
        else:
            new_seeds.append((start_1, end_1))
    new_seeds.append(seeds[-1])
    if seeds != new_seeds:
        print("joined", new_seeds)
    return new_seeds

def test():
    print(
        run(
            """seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4"""
        )
    )
if __name__ == "__main__":
    print(run(open("src/2023/data/days/05/data", "r").read()))
