from functools import lru_cache

directions = [
    (-1j, (3, 4, 5)),
    (1j, (0, 1, 2)),
    (-1, (2, 5, 7)),
    (1, (1, 4, 6)),
]

all_nearby = [1j, 1 + 1j, -1 + 1j, -1j, 1 - 1j, -1 - 1j, 1, -1]
elves = set()


def read_data(input_data):
    global elves
    for y, row in enumerate(input_data.splitlines()):
        for x, char in enumerate(row):
            if char == "#":
                elves.add(complex(x, y))


def run(input_data, rounds):
    read_data(input_data)
    for step in range(rounds):
        if move(step):
            break
    return count_tiles(elves)


def move(step):
    global elves
    proposed_steps = {}
    elf_conflicts = set()
    for pos in elves:
        nearby_elves = [check_pos(pos + nearby, step) for nearby in all_nearby]
        if True in nearby_elves:
            for i in range(step, step + 4):
                direction, nearby_indexes = directions[i % 4]
                if elf_move_available(nearby_indexes, tuple(nearby_elves)):
                    elf_next_step = pos + direction
                    if elf_next_step not in elf_conflicts:
                        if elf_next_step in proposed_steps:
                            elf_conflicts.add(elf_next_step)
                            del proposed_steps[elf_next_step]
                        else:
                            proposed_steps[elf_next_step] = pos
                    break
    for next_pos, pos in proposed_steps.items():
        elves.remove(pos)
        elves.add(next_pos)
    return len(proposed_steps) == 0


@lru_cache
def elf_move_available(nearby_indexes, nearby_elves):
    for nearby_index in [*nearby_indexes]:
        if nearby_elves[nearby_index]:
            return False
    return True


@lru_cache
def check_pos(pos, step):
    return pos in elves


def count_tiles(elves):
    elves_y = [int(elf.imag) for elf in elves]
    elves_x = [int(elf.real) for elf in elves]
    counter = 0
    for y in range(min(elves_y), max(elves_y) + 1):
        for x in range(min(elves_x), max(elves_x) + 1):
            if complex(x, y) not in elves:
                counter += 1
    return counter


if __name__ == "__main__":
    print(run(open("src/2022/data/days/23/data", "r").read(), 10))
