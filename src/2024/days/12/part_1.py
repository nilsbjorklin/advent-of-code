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


def calculate_connected(region):
    connected = 0
    for plot in region:
        for direction in directions:
            if plot + direction in region:
                connected += 1
    return connected


def run(input_data: list[str]):
    regions = read_data(input_data)
    result = 0
    for region in regions:
        plots_count = len(region)
        connected_count = calculate_connected(region)
        result += plots_count * (4 * plots_count - connected_count)
    return result


if __name__ == '__main__':
    print(run(open('src/2024/data/days/12/data', 'r').readlines()))
