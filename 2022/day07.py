inputs = [i.strip() for i in open("inputs/day07.txt", 'r').readlines()]

dirs = {"/": {}}
cur_path = ["/"]

# lol, lmao
idx = 0
while idx < len(inputs):
    line = inputs[idx]
    if line.startswith("$ "):
        line = line[2:]
        if line.startswith("ls"):
            files = []
            while True:
                idx += 1
                if idx >= len(inputs):
                    break
                subline = inputs[idx]
                if subline.startswith("$"):
                    idx -= 1
                    break
                files.append(subline)
            subdir = dirs
            for i in cur_path:
                subdir = subdir[i]
            for file in files:
                size, name = file.split(" ")
                if size == "dir":
                    subdir[name] = {}
                else:
                    size = int(size)
                    subdir[name] = size

        elif line.startswith("cd "):
            line = line[3:]
            param = line
            if param == "/":
                cur_path = ["/"]
            elif param == "..":
                cur_path = cur_path[:-1]
            else:
                cur_path = cur_path + [param]
    idx += 1


part_1 = 0

def resolve_size_p1(path, first=False):
    global part_1
    total_size = 0
    for i in path:
        v = path[i]
        if isinstance(v, dict):
            total_size += resolve_size_p1(v)
        else:
            total_size += v
    if total_size < 100_000 and not first:
        part_1 += total_size
    return total_size
total_size = resolve_size_p1(dirs, True)

print(f"part 1: {part_1}")

free_space = 70000000 - total_size
space_needed = 30000000 - free_space

part_2 = 9999999999999999
def resolve_size_p2(path, first=False):
    global part_2
    total_size = 0
    for i in path:
        v = path[i]
        if isinstance(v, dict):
            total_size += resolve_size_p2(v)
        else:
            total_size += v
    if total_size > space_needed and not first:
        part_2 = min(part_2, total_size)
    return total_size
resolve_size_p2(dirs, True)
print(f"part 2: {part_2}")
