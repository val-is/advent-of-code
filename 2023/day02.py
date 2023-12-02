lines = [i for i in open('inputs/day02.txt', 'r').readlines()]

part1 = 0
part2 = 0

for game, line in enumerate(lines):
    line = line.split(":")[1].split("; ")
    p = True
    ns = {}
    for gg in line:
        gg = gg.split(", ")
        nsp1 = {}
        for l in gg:
            num, color = l.strip().split(" ")
            num = int(num)
            nsp1[color] = num
            if color not in ns:
                ns[color] = num
            else:
                ns[color] = max(ns[color], num)
        for n in nsp1:
            if n == "red" and nsp1[n] > 12:
                p = False
            elif n == "green" and nsp1[n] > 13:
                p = False
            elif n == "blue" and nsp1[n] > 14:
                p = False
    if p:
        part1 += game+1
    part2 += ns["red"]*ns["blue"]*ns["green"]

print(f"part 1:")
print(f"{part1}")

print(f"part 2:")
print(f"{part2}")