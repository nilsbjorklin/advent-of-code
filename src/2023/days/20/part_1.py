from collections import deque
import re

flip_flop = {}
conjunction = {}
broadcaster = []
pulses_sent = {False: 0, True: 0}


def read_data(input_data):
    global flip_flop, conjunction, broadcaster
    pattern = re.compile(r"(\w+)")
    for row in input_data.splitlines():
        matches = pattern.findall(row)
        if row.startswith("%"):
            flip_flop[matches[0]] = {"targets": matches[1:], "is_on": False}
        if row.startswith("&"):
            conjunction[matches[0]] = {"targets": matches[1:], "inputs": {}}
        if matches[0] == "broadcaster":
            broadcaster = [target for target in matches[1:]]
    for name in conjunction.keys():
        for k, value in flip_flop.items():
            if name in value["targets"]:
                conjunction[name]["inputs"][k] = False


def run(input_data, button_presses):
    read_data(input_data)
    for _ in range(button_presses):
        press_button()
    low, high = pulses_sent.values()
    return low * high


def press_button():
    global flip_flop, conjunction, broadcaster, pulses_sent
    pulses = deque()
    pulses.append(("button", "broadcaster", False))
    pulses_sent[False] += 1

    while len(pulses) != 0:
        source, target, signal = pulses.popleft()

        if target == "broadcaster":
            next_targets = broadcaster

            for next_target in next_targets:
                pulses.append((target, next_target, False))
                pulses_sent[False] += 1

        elif not signal and target in flip_flop:
            next_targets = flip_flop[target]["targets"]
            on_off = flip_flop[target]["is_on"]
            on_off = not on_off
            flip_flop[target]["is_on"] = on_off

            for next_target in next_targets:
                pulses.append((target, next_target, on_off))
                pulses_sent[on_off] += 1

        elif target in conjunction:
            next_targets = conjunction[target]["targets"]
            conjunction[target]["inputs"][source] = signal
            last_signal_high = True
            for last_signal in conjunction[target]["inputs"].values():
                if not last_signal:
                    last_signal_high = False
                    break

            next_signal = not last_signal_high

            for next_target in next_targets:
                pulses.append((target, next_target, next_signal))
                pulses_sent[next_signal] += 1


if __name__ == "__main__":
    print(run(open("src/2023/data/days/20/data", "r").read(), 1000))
