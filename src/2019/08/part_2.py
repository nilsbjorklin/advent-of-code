def read_data(input_data, width, height):
    total_size = width * height
    return [
        input_data[i: i + total_size] for i in range(0, len(input_data), total_size)
    ]


def run(input_data, width, height) -> None:
    layers = read_data(input_data, width, height)
    result = []
    for row in range(height):
        for col in range(width):
            index = row * width + col
            for layer in layers:
                pixel_value = layer[index]
                if pixel_value != "2":
                    result.append(" " if pixel_value == "0" else "#")
                    break
    for index in range(0, len(result), width):
        print("".join(result[index: index + width]))


if __name__ == "__main__":
    run(open("data").read(), 25, 6)
