import time

def time_method(name, method, *args, **kwargs):
    start_time = time.perf_counter()
    result = method(*args, **kwargs)
    end_time = time.perf_counter()

    print(f"'{name}' Duration: {(end_time - start_time) * 1000:.0f} ms")

    return result


def print_2d(width, height, icon_dict: dict[complex, str], default='.'):
    result = []
    for height_idx in range(0, height):
        row = ''
        for width_idx in range(0, width):
            icon = default
            if width_idx + height_idx * 1j in icon_dict:
                icon = icon_dict[width_idx + height_idx * 1j]
            row += icon
        result.append(row)
    print('\n'.join(result))
