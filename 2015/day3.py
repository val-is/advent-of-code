data = open('inputs/day3.txt', 'r').read()

instructions = []
for i in data:
    if i == '^':
        instructions += [(0, 1)]
    elif i == 'v':
        instructions += [(0, -1)]
    elif i == '<':
        instructions += [(-1, 0)]
    elif i == '>':
        instructions += [(1, 0)]

# part 1
houses_visited = {(0, 0)}
x, y = 0, 0
for instr in instructions:
    x += instr[0]
    y += instr[1]
    houses_visited.add((x, y))
print(f"part 1: {len(houses_visited)}")

# part 2
houses_visited = {(0, 0)}
s_x, s_y = 0, 0
r_x, r_y = 0, 0
santa_turn = True
for instr in instructions:
    dx, dy = instr
    if santa_turn:
        s_x += dx
        s_y += dy
        houses_visited.add((s_x, s_y))
    else:
        r_x += dx
        r_y += dy
        houses_visited.add((r_x, r_y))
    santa_turn = not santa_turn
print(f"part 2: {len(houses_visited)}")
