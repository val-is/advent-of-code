dat = [i.strip() for i in open("inputs/day04.txt", "r").readlines()]

charmap = {}
ma_x = 0
ma_y = 0
for y, row in enumerate(dat):
    ma_y = max(ma_y, y)
    for x, val in enumerate(row):
        ma_x = max(ma_x, x)
        charmap[x, y] = val

part1 = 0
part2 = 0


def check_xmas(pos, delta):
    build = ""
    for i in range(4):
        new_pos = (pos[0] + delta[0] * i, pos[1] + delta[1] * i)
        build += charmap.get(new_pos, ".")
    return build == "XMAS"


def check_xxmas(pos, delta):
    a = charmap.get((pos[0] - 1, pos[1] - 1), ".")
    b = charmap.get((pos[0] + 1, pos[1] - 1), ".")
    c = charmap.get((pos[0], pos[1]), ".")
    d = charmap.get((pos[0] - 1, pos[1] + 1), ".")
    e = charmap.get((pos[0] + 1, pos[1] + 1), ".")
    if a == "M" and b == "S" and c == "A" and d == "M" and e == "S":
        return True
    if a == "M" and b == "M" and c == "A" and d == "S" and e == "S":
        return True
    if a == "S" and b == "S" and c == "A" and d == "M" and e == "M":
        return True
    if a == "S" and b == "M" and c == "A" and d == "S" and e == "M":
        return True
    return False


for x in range(ma_x + 1):
    for y in range(ma_y + 1):
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dx == dy == 0:
                    continue
                if check_xmas((x, y), (dx, dy)):
                    part1 += 1
        if check_xxmas((x, y), (0, 0)):
            part2 += 1


print(f"part 1:")
print(f"{part1}")

print(f"part 2:")
print(f"{part2}")
