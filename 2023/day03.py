lines = [i for i in open('inputs/day03.txt', 'r').readlines()]

m = {}
m_ids = {}
tile_id = 0
for y, row in enumerate(lines):
    int_building = ""
    updating_tiles = []
    for x, val in enumerate(row.strip()):
        if val not in "1234567890":
            if len(updating_tiles) != 0:
                for tile in updating_tiles:
                    m[tile] = int(int_building)
                    m_ids[tile] = tile_id
                tile_id += 1
            m[x, y] = val
            updating_tiles = []
            int_building = ""
        else:
            int_building += val
            updating_tiles.append((x, y))
    if len(updating_tiles) != 0:
        for tile in updating_tiles:
            m[tile] = int(int_building)
            m_ids[tile] = tile_id
        tile_id += 1
    updating_tiles = []
    int_building = ""

part1 = 0
for coord in m:
    s = 0
    if m[coord] != "." and type(m[coord]) != int:
        ids_added = []
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dx == dy == 0:
                    continue
                dd = (coord[0]+dx, coord[1]+dy)
                if dd not in m:
                    continue
                if type(m[dd]) == int:
                    if m_ids[dd] in ids_added:
                        continue
                    ids_added.append(m_ids[dd])
                    s += m[dd]
    part1 += s

part2 = 0
for coord in m:
    if m[coord] == "*":
        ids_added = []
        adjs = []
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dx == dy == 0:
                    continue
                dd = (coord[0]+dx, coord[1]+dy)
                if dd not in m:
                    continue
                if type(m[dd]) == int:
                    if m_ids[dd] in ids_added:
                        continue
                    ids_added.append(m_ids[dd])
                    adjs.append(m[dd])
        if len(adjs) != 2:
            continue
        r = adjs[0] * adjs[1]
        part2 += r

print(f"part 1:")
print(f"{part1}")

print(f"part 2:")
print(f"{part2}")