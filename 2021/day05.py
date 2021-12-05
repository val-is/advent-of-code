inputs = [i for i in open('inputs/day05.txt', 'r').readlines()]

vents = []
for i in inputs:
    f = lambda x: [int(i) for i in x.split(",")]
    vents.append([f(x) for x in i.split(" -> ")])

def is_horiz(vent):
    a, b = vent
    x1, y1 = a
    x2, y2 = b
    if x1 == x2 and y1 != y2:
        return True
    if x1 != x2 and y1 == y2:
        return True
    return False

def get_points_covered(vent):
    tiles = set()
    
    a, b = vent
    x1, y1 = a
    x2, y2 = b
    
    getsign = lambda i: 1 if i > 0 else -1
    dx = getsign(x2 - x1)
    dy = getsign(y2 - y1)
    
    if x1 == x2:
        ymin, ymax = sorted([y1, y2])
        for y in range(ymin, ymax+1):
            tiles.add((x1, y))
    elif y1 == y2:
        xmin, xmax = sorted([x1, x2])
        for x in range(xmin, xmax+1):
            tiles.add((x, y1))
    else:
        d = abs(x2 - x1)
        for r in range(0, d+1):
            tiles.add((x1+dx*r, y1+dy*r))
    return tiles

def get_tiles(vents):
    points_covered = {}
    for i in vents:
        for point in get_points_covered(i):
            points_covered[point] = points_covered.get(point, 0) + 1
    return points_covered

def count_tiles(tiles):
    return len([p for p in tiles if tiles[p] >= 2])

part1 = count_tiles(get_tiles([i for i in vents if is_horiz(i)]))
print(f"part 1: {part1}")

part2 = count_tiles(get_tiles(vents))
print(f"part 2: {part2}")
