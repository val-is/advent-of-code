inputs = [i.strip() for i in open("inputs/day08.txt", 'r').readlines()]

heights = {}
ma_x = 0
ma_y = 0
for y, row in enumerate(inputs):
    ma_y = max(ma_y, y)
    for x, col in enumerate(row):
        heights[(x, y)] = int(col)
        ma_x = max(ma_x, x)
ma_x += 1
ma_y += 1

trees = set()
for x in range(ma_x):
    ma_h = -1
    for y in range(ma_y):
        h = heights[(x, y)]
        if h > ma_h:
            trees.add((x, y))
            ma_h = h
    ma_h = -1
    for y in range(ma_y)[::-1]:
        h = heights[(x, y)]
        if h > ma_h:
            trees.add((x, y))
            ma_h = h

for y in range(ma_y):
    ma_h = -1
    for x in range(ma_x):
        h = heights[(x, y)]
        if h > ma_h:
            trees.add((x, y))
            ma_h = h
    ma_h = -1
    for x in range(ma_x)[::-1]:
        h = heights[(x, y)]
        if h > ma_h:
            trees.add((x, y))
            ma_h = h
part_1 = len(trees)
print(f"part 1: {part_1}")

dirs = [(-1, 0), (0, -1), (1, 0), (0, 1)]
def get_view_dist(x, y):
    dists = []
    for dir in dirs:
        dx, dy = dir
        cur_pos = (x+dx, y+dy)
        dist = 0
        height = heights[(x, y)]
        while cur_pos in heights:
            dist += 1
            if heights[cur_pos] >= height:
                break
            cur_pos = (cur_pos[0] + dx, cur_pos[1] + dy)
        dists.append(dist)
    return dists[0]*dists[1]*dists[2]*dists[3]

part_2 = max([get_view_dist(*i) for i in heights])
print(f"part 2: {part_2}")
