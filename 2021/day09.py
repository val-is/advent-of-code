inputs = open('inputs/day09.txt', 'r').readlines()

def load_map(inputs):
    heightmap = {}
    for y, row in enumerate(inputs):
        for x, val in enumerate(row.strip()):
            heightmap[(x, y)] = int(val)
    return heightmap

def get_adjacent(pos):
    return {
            (pos[0]+1, pos[1]),
            (pos[0]-1, pos[1]),
            (pos[0], pos[1]+1),
            (pos[0], pos[1]-1),
            }

def get_low_points(heightmap):
    lowpoints = set()
    for pos in heightmap:
        height = heightmap[pos]
        neighbors = get_adjacent(pos)
        lowpoint = True
        for n in [i for i in neighbors if i in heightmap]:
            if heightmap[n] <= height:
                lowpoint = False
        if lowpoint:
            lowpoints.add(pos)
    return lowpoints

def get_risk_level(heightmap, point):
    return heightmap[point] + 1

heightmap = load_map(inputs)
lowpoints = get_low_points(heightmap)

part1 = sum([get_risk_level(heightmap, i) for i in lowpoints])
print(f"part 1: {part1}")

def expand_basin(heightmap, point, traversed):
    if point not in traversed:
        traversed.add(point)
    adj = get_adjacent(point)
    for a in [i for i in adj if i in heightmap]:
        if heightmap[a] != 9 and a not in traversed:
            traversed.add(a)
            expand_basin(heightmap, a, traversed)
    return traversed

basins = []

for point in lowpoints:
    find_basin = True
    for b in basins:
        if point in b:
            find_basin = False
    if not find_basin:
        continue
    basin = expand_basin(heightmap, point, set())
    basins.append(basin)

def get_basin_size(basin):
    return len(basin)

part2 = 1
sizes = sorted([len(b) for b in basins])[::-1][:3]
for s in sizes:
    part2 *= s
print(f"part 2: {part2}")
