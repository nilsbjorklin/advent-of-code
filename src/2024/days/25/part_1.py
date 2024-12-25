def read_data(input_data):
    keys_and_locks = input_data.strip().split("\n\n")
    keys = []
    locks = []
    for key_or_lock in keys_and_locks:
        if key_or_lock[0] == "#":
            lock = []
            for i in range(5):
                for index, line in enumerate(key_or_lock.splitlines()):
                    if line[i] == ".":
                        lock.append(index)
                        break
            locks.append(lock)
            pass
        else:
            key = []
            for i in range(5):
                for index, line in enumerate(key_or_lock.splitlines()):
                    if line[i] == "#":
                        key.append(index)
                        break
            keys.append(key)
    return keys, locks


def run(input_data):
    keys, locks = read_data(input_data)
    result = 0
    for key in keys:
        for lock in locks:
            if key_fits_in_lock(key, lock):
                result += 1
    return result

def key_fits_in_lock(key, lock):
    for i in range(5):
        if lock[i] > key[i]:
            return False
    return True


if __name__ == "__main__":
    print(run(open("src/2024/data/days/25/data", "r").read()))
