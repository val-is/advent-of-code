inputs = open('inputs/day15.txt', 'r').read()

def read_map(inputs):
    m = {}
    for y, row in enumerate(inputs.split("\n")):
        for x, val in enumerate(row.strip()):
            m[x, y] = int(val)
    return m

def get_adj(p):
    return [
            (p[0]+1, p[1]),
            (p[0]-1, p[1]),
            (p[0], p[1]+1),
            (p[0], p[1]-1),
            ]

def traverse(m, max_tile):
    dists = {(0,0): 0}
    tiles = [(0, 0)]
    while len(tiles) > 0:
        tiles = sorted(tiles, key=lambda x: dists[x])
        tile = tiles[0]
        for adj in get_adj(tile):
            if adj not in m:
                continue
            risk = dists[tile] + m[adj]
            if adj in dists and risk < dists[adj]:
                dists[adj] = risk
            elif adj not in dists:
                dists[adj] = risk
                tiles.append(adj)
        tiles.pop(0)

    return dists[max_tile]

def conv_p2(m, max_tile):
    n_m = {}
    for x in range(5):
        for y in range(5):
            for i in range(max_tile[0]+1):
                for j in range(max_tile[1]+1):
                    val = m[i, j] + x + y
                    if val >= 10:
                        val -= 9
                    n_m[i + (max_tile[0]+1) * x, j + (max_tile[1]+1) * y] = val
    return n_m


m = read_map(inputs)
p2m = conv_p2(m, (99,99))

part1 = traverse(m, (99, 99))
print(f"part 1: {part1}")

part2 = traverse(p2m, (100*5-1, 100*5-1))
print(f"part 2: {part2}")
