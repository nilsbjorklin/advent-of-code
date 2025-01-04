def read_data(input_data):
    return [row.strip().splitlines() for row in input_data.split("$")[1:]]


def run(input_data):
    terminal = read_data(input_data)
    current_dir = []
    dirs = {}
    for terminal_section in terminal:
        command = terminal_section[0]
        if len(terminal_section) == 1:
            if command.startswith('cd'):
                move_target = command[2:].strip()
                if move_target == "..":
                    del current_dir[-1]
                elif move_target == "/":
                    current_dir.clear()
                else:
                    current_dir.append(move_target)
        for ls_output in terminal_section[1:]:
            ls_output = ls_output.split(" ")[0]
            if ls_output.isdigit():
                for path in paths(current_dir):
                    if path not in dirs:
                        dirs[path] = 0
                    dirs[path] += int(ls_output)
    return sum(size if size <= 100000 else 0 for size in dirs.values())
        
            
def paths(dirs):
    if len(dirs) == 0:
        return ["/"]
    return ["/".join(dirs)] + paths(dirs[:-1])


if __name__ == "__main__":
    print(run(open("src/2022/data/days/07/data", "r").read()))
