from functools import lru_cache


def read_data(input_data: str) -> set:
    active_cubes = set()
    for y, row in enumerate(input_data.splitlines()):
        for x, value in enumerate(row):
            if value == "#":
                active_cubes.add((x, y, 1))
    return active_cubes


def run(input_data: str, limit: int) -> int:
    active_cubes = read_data(input_data)
    for i in range(limit):
        new_active = set()
        all_nearby_cubes = {}
        for cube in active_cubes:
            cubes = nearby_cubes(*cube)
            for nearby_cube in cubes:
                if nearby_cube not in all_nearby_cubes:
                    all_nearby_cubes[nearby_cube] = 0
                all_nearby_cubes[nearby_cube] += 1
            nearby_active_cubes = len(cubes.intersection(active_cubes))
            if nearby_active_cubes == 2 or nearby_active_cubes == 3:
                new_active.add(cube)
        for pos, count in all_nearby_cubes.items():
            if count == 3:
                new_active.add(pos)
        active_cubes = new_active
    return len(active_cubes)


@lru_cache
def nearby_cubes(x, y, z):
    nearby = set()
    for x_change in range(-1, 2):
        for y_change in range(-1, 2):
            for z_change in range(-1, 2):
                nearby.add((x + x_change, y + y_change, z + z_change))
    nearby.remove((x, y, z))
    return nearby


if __name__ == "__main__":
    print(run(open("data", "r").read(), 6))
