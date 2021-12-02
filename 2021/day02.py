inputs = [i.strip().split() for i in open('inputs/day02.txt', 'r').readlines()]

instrs = []
for i in inputs:
    instrs.append([i[0], int(i[1])])

horiz = 0
vert = 0
vert_aiming = 0
aim = 0

for i in instrs:
    dir, amount = i
    if dir == 'forward':
        horiz += amount
        vert_aiming += amount * aim
    if dir == 'up':
        aim -= amount
        vert -= amount
    if dir == 'down':
        aim += amount
        vert += amount

part1 = horiz * vert
print(f"part 1: {part1}")

part2 = horiz * vert_aiming
print(f"part 2: {part2}")

