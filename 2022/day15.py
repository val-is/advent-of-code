inputs = [i.strip() for i in open('inputs/day15.txt', 'r').readlines()]

sensors = []

def extract_num(s):
    return int(s.split("=")[1].replace(':', '').replace(',', ''))

for line in inputs:
    ll = line.strip().split(" ")
    sx, sy, bx, by = [extract_num(ll[i]) for i in [2, 3, 8, 9]]
    sensors.append(((sx, sy), (bx, by)))

def get_dist(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

covered_tiles = {}
beacon_tiles = {}
row_check = 2000000
for sensor in sensors:
    s_pos, b_pos = sensor

    beacon_tiles[b_pos] = True
    dist = get_dist(s_pos, b_pos)
    dy = row_check - s_pos[1]
    for dx in range(-dist, dist+1):
        if get_dist((s_pos[0]+dx, s_pos[1]+dy), s_pos) <= dist:
            covered_tiles[(s_pos[0]+dx, s_pos[1]+dy)] = True

s = 0
for tile in covered_tiles:
    if tile[1] == row_check and tile not in beacon_tiles:
        s += 1


part1 = s
print(f"part 1: {part1}")

r_max = 4_000_000
for y in range(0, r_max+1):
    row_ranges = []
    for s_pos, b_pos in sensors:
        b_dist = get_dist(s_pos, b_pos)
        dist = b_dist - abs(s_pos[1] - y)
        if dist <= 0:
            continue
        mi, ma = s_pos[0]-dist, s_pos[0]+dist
        row_ranges.append((mi, ma))
    while True:
        updated = False
        for k1, range_1 in enumerate(row_ranges):
            for k2, range_2 in enumerate(row_ranges):
                if k1 == k2:
                    continue
                if range_1[0] <= range_2[0] <= range_2[1] <= range_1[1]: # range 2 in range 1
                    row_ranges.remove(range_2)
                    updated = True
                    break
                if range_2[0] <= range_1[0] <= range_1[1] <= range_2[1]: # range 1 in range 2
                    row_ranges.remove(range_1)
                    updated = True
                    break
                # range 2 and range 1 overlap, 1 <= 2 <= 1 <= 2
                if range_1[0] <= range_2[0] <= range_1[1] <= range_2[1]:
                    row_ranges.remove(range_2)
                    row_ranges.remove(range_1)
                    row_ranges.append((range_1[0], range_2[1]))
                    updated = True
                    break
                # range 2 and range 1 overlap, 2 <= 1 <= 2 <= 1
                if range_2[0] <= range_1[0] <= range_2[1] <= range_1[1]:
                    row_ranges.remove(range_2)
                    row_ranges.remove(range_1)
                    row_ranges.append((range_2[0], range_1[1]))
                    updated = True
                    break
                # no overlap!! pogging and found solution (maybe)
        if not updated:
            if len(row_ranges) > 1:
                a, b = row_ranges[:2]
                target_x = max(a[0], b[0])-1
                print(f"part 2: {4_000_000 * target_x + y}")
                import sys
                sys.exit(0)
            break
