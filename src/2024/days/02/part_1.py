def read_data(input_data):
    result = []
    for line in input_data:
        parts = line.strip().split()
        result.append([int(part) for part in parts])
    return result


def run(input_data: list[str]):
    safe_report_count = 0
    for report in read_data(input_data):
        invalid_report = report[0] == report[1]
        if not invalid_report:
            valid_range = range(1, 4) if report[0] < report[1] else range(-3, 0)
            for i in range(1, len(report)):
                if report[i] - report[i - 1] not in valid_range:
                    invalid_report = True
                    break
        if not invalid_report:
            safe_report_count += 1
    return safe_report_count


if __name__ == '__main__':
    print(run(open('src/2024/data/days/02/data', 'r').readlines()))
