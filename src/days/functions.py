import time


def time_method(name, method, *args, **kwargs):
    start_time = time.perf_counter()
    result = method(*args, **kwargs)
    end_time = time.perf_counter()

    print(f"'{name}' Duration: {(end_time - start_time) * 1000:.0f} ms")

    return result
