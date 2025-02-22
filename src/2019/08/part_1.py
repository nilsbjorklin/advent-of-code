def read_data(input_data, width, height):
    total_size = width * height
    return [
        input_data[i: i + total_size] for i in range(0, len(input_data), total_size)
    ]


def run(input_data, width, height) -> int:
    layers = read_data(input_data, width, height)
    result = 0
    fewest_zeros = None
    for index, layer in enumerate(layers):
        zeroes_count = layer.count("0")
        if fewest_zeros is None or zeroes_count < fewest_zeros:
            fewest_zeros = zeroes_count
            result = layer.count("1") * layer.count("2")
    return result


if __name__ == "__main__":
    print(run(open("data").read(), 25, 6))
