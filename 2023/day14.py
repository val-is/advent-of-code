def iter_north(rocks, max_x, max_y):
    for y in range(1, max_y+1):
        for x in range(max_x+1):
            if rocks[x, y] == "O" and rocks[x, y-1] == ".":
                rocks[x, y] = "."
                rocks[x, y-1] = "O"
    return rocks

def iter_south(rocks, max_x, max_y):
    for y in range(max_y)[::-1]:
        for x in range(max_x+1):
            if rocks[x, y] == "O" and rocks[x, y+1] == ".":
                rocks[x, y] = "."
                rocks[x, y+1] = "O"
    return rocks

def iter_west(rocks, max_x, max_y):
    for x in range(1, max_x+1):
        for y in range(max_y+1):
            if rocks[x, y] == "O" and rocks[x-1, y] == ".":
                rocks[x, y] = "."
                rocks[x-1, y] = "O"
    return rocks

def iter_east(rocks, max_x, max_y):
    for x in range(max_x)[::-1]:
        for y in range(max_y+1):
            if rocks[x, y] == "O" and rocks[x+1, y] == ".":
                rocks[x, y] = "."
                rocks[x+1, y] = "O"
    return rocks

def hash_rocks(rocks, max_x, max_y):
    bm = 0
    cc = 0
    for y in range(max_y+1):
        for x in range(max_x+1):
            if rocks[x, y] == "O":
                bm |= 1<<cc
            cc += 1
    return bm

def render(rocks, max_x, max_y):
    for y in range(max_y+1):
        for x in range(max_x+1):
            print(rocks[x, y], end="")
        print()
    print()

cache = {}
def spin(rocks, max_x, max_y, caching=True):
    r_hash = hash_rocks(rocks, max_x, max_y)
    if r_hash in cache and caching:
        return rocks, True
    for _ in range(max_y+1):
        rocks = iter_north(rocks, max_x, max_y)
    # render(rocks, max_x, max_y)
    for _ in range(max_x+1):
        rocks = iter_west(rocks, max_x, max_y)
    # render(rocks, max_x, max_y)
    for _ in range(max_y+1):
        rocks = iter_south(rocks, max_x, max_y)
    # render(rocks, max_x, max_y)
    for _ in range(max_x+1):
        rocks = iter_east(rocks, max_x, max_y)
    # render(rocks, max_x, max_y)
    # assert False
    cache[r_hash] = {k: rocks[k] for k in rocks}
    return rocks, False

def calc_load(rocks, max_x, max_y):
    load = 0
    for y in range(max_y+1):
        for x in range(max_x+1):
            if rocks[x, y] == "O":
                load += (max_y-y)+1
    return load

def run(fname):
    lines = [f for f in open(fname, 'r').readlines()]
    
    rocks = {}
    max_x = 0
    max_y = 0
    for y, row in enumerate(lines):
        for x, v in enumerate(row):
            rocks[x, y] = v
            max_x = x
        max_y = y
    rocks_p1 = {k: rocks[k] for k in rocks}
    for _ in range(max_y+1):
        iter_north(rocks_p1, max_x, max_y)
    part1 = calc_load(rocks_p1, max_x, max_y)

    total = 0
    hit = None
    for i in range(1000000000):
        rocks, cache_hit = spin(rocks, max_x, max_y)
        total+=1
        if cache_hit:
            hit = i
            break
    print(hit)
    global cache
    cache = {}
    for i in range(i, 1000000000):
        rocks, cache_hit = spin(rocks, max_x, max_y)
        total+=1
        if cache_hit:
            hit = i
            break
    print(hit)
    cache = {}
    for i in range(i, 1000000000):
        rocks, cache_hit = spin(rocks, max_x, max_y)
        total+=1
        if cache_hit:
            hit = i
            break
    print(hit)
    hit_a = hit
    cache = {}
    for i in range(i, 1000000000):
        rocks, cache_hit = spin(rocks, max_x, max_y)
        total+=1
        if cache_hit:
            hit = i
            break
    print(hit)
    period = hit-hit_a
    print(period)
    for _ in range((1000000000-total+4)%period):
        rocks, _ = spin(rocks, max_x, max_y, caching=False)
    
    part2 = calc_load(rocks, max_x, max_y)

    print(f"part 1:")
    print(f"{part1}")

    print(f"part 2:")
    print(f"{part2}")

print("TEST")
run('inputs/test.txt')
print()
print("REAL")
run('inputs/day14.txt')