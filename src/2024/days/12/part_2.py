from collections import defaultdict

directions = [1, 1j, -1, -1j]


def read_data(input_data):
    data = {
        (col_idx + row_idx * 1j, col)
        for row_idx, row in enumerate(input_data)
        for col_idx, col in enumerate(row.strip())
    }
    regions = set()
    visited_plots = set()
    for plot in data:
        if plot not in visited_plots:
            regions.add(travel_region(plot, data, set(), visited_plots))
    return regions


def travel_region(plot, data, region, visited_plots):
    if plot not in visited_plots:
        pos, value = plot
        region.add(pos)
        visited_plots.add(plot)
        for direction in directions:
            next_plot = (pos + direction, value)
            if next_plot in data:
                travel_region(next_plot, data, region, visited_plots)
    return tuple(region)


def calculate_sides(region):
    sides = defaultdict(list)
    for plot in region:
        for direction in directions:
            target = plot + direction
            if target not in region:
                if direction.imag != 0:
                    sides[
                        (int(direction.real), int(direction.imag), int(plot.imag))
                    ].append((int(plot.real)))
                else:
                    sides[
                        (int(direction.real), int(direction.imag), int(plot.real))
                    ].append((int(plot.imag)))

    return sum(
        [
            1 if (j - i) > 1 else 0
            for plots in sides.values()
            for i, j in zip(sorted(plots)[:-1], sorted(plots)[1:])
        ]
        + [len(sides)]
    )


def run(input_data: list[str]):
    regions = read_data(input_data)
    result = 0
    for region in regions:
        plots_count = len(region)
        sides_count = calculate_sides(region)
        result += plots_count * sides_count
    return result


if __name__ == "__main__":
    print(run(open("src/2024/data/days/12/data", "r").readlines()))
