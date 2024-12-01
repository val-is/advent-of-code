import sys
# sys.setrecursionlimit(15000)

def iter(filled, filled_keys, ignoring=None, forcing=None):
    blocks_moving = set()
    blocks_not_moving = set()
    blocks = set(filled_keys.values())
    for block in filled:
        x, y, z = block
        if filled_keys[block] == ignoring:
            continue
        if z == 1:
            blocks_not_moving.add(filled_keys[block])
            continue
        if filled_keys.get((x, y, z-1), -1) == ignoring:
            continue
        if filled.get((x, y, z-1), False) == True and filled_keys[block] != filled_keys.get((x, y, z-1), -1):
            blocks_not_moving.add(filled_keys[block])
            continue
    
    blocks_moving = blocks - blocks_not_moving
    blocks_moving -= {ignoring}
    
    next_filled = {}
    next_filled_keys = {}
    for block in filled:
        x,y,z = block
        if filled_keys[block] in blocks_moving:
            next_filled[x,y,z-1] = filled[block]
            next_filled_keys[x,y,z-1] = filled_keys[block]
        else:
            next_filled[x,y,z] = filled[block]
            next_filled_keys[x,y,z] = filled_keys[block]
    return next_filled, next_filled_keys, blocks_moving

def recur_get(falling, target):
    s = 0
    for k in falling[target]:
        s += falling[k]
    return s

DP = {}
def stable(filled, filled_keys, ignoring=None):
    if ignoring in DP:
        return DP[ignoring]
    fn = {k: filled[k] for k in filled}
    fk = {k: filled_keys[k] for k in filled_keys}
    updated = True
    moved = set()
    while updated:
        fn, fk, updated = iter(fn, fk, ignoring)
        moved |= updated
    DP[ignoring] = moved
    return moved

def run(fname):
    lines = [line for line in open(fname, 'r').readlines()]

    filled = {}
    filled_keys = {}

    for k, line in enumerate(lines):
        a,b = line.strip().split("~")
        x1,y1,z1 = map(int, a.split(","))
        x2,y2,z2 = map(int, b.split(","))

        for x in range(x1, x2+1):
            for y in range(y1, y2+1):
                for z in range(z1, z2+1):
                    filled[x,y,z] = True
                    filled_keys[x,y,z] = k

    updated = True
    while updated:
        filled, filled_keys, updated = iter(filled, filled_keys)

    part1 = 0
    part2 = 0

    drops = []
    for block_key in set(filled_keys.values()):
        _, _, updated = iter(filled, filled_keys, ignoring=block_key)
        if len(updated) == 0:
            part1 += 1
        else:
            drops.append(block_key)

    
    for d in drops:
        updated = stable(filled, filled_keys, ignoring=d)
        part2 += len(updated)

    
    print(f"part 1:")
    print(f"{part1}")

    print(f"part 2:")
    print(f"{part2}")

print("TEST")
run('inputs/test.txt')
print()
print("REAL")
run('inputs/day22.txt')