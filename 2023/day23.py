import sys
sys.setrecursionlimit(3000)

deltas = [
    (-1, 0),
    (1, 0),
    (0, -1),
    (0, 1),
]

def render(visited, max_x, max_y):
    for y in range(max_y+1):
        for x in range(max_x+1):
            if (x, y) in visited:
                print("O", end="")
            else:
                print("#", end="")
        print()
    print()

DP = {}
DPvisited = {}
max_x = max_y = 0
max_loop_dist = 0
def traverse(mm, coord, distance=0, visited=set(), force_to_next_junc=False, end_coord=None):
    global DPvisited
    global DP
    global max_loop_dist
    if distance == 0:
        DP = {}
        DPvisited = {}
        max_loop_dist = 0
    if not force_to_next_junc:
        if coord in DP:
            if DP[coord] >= distance and 0.5*(DP[coord]-distance) > max_loop_dist:
                return
        
        if coord in DP:
            DP[coord] = max(DP[coord], distance)
        else:
            DP[coord] = distance

    visited |= {coord}

    adjs = []
    for dx, dy in deltas:
        adj = (coord[0]+dx, coord[1]+dy)
        if adj not in mm:
            continue
        if mm[adj] == "#":
            continue
        if adj in visited:
            if max_loop_dist < distance-DP[adj]:
                print(distance-DP[adj])
                if end_coord:
                    if end_coord in DP:
                        print(f">> {DP[end_coord]}")
            max_loop_dist = max(distance-DP[adj], max_loop_dist)
            continue
        adjs.append(adj)
    if mm[coord] in "><v^":
        dx, dy = {
            ">": (1, 0),
            "<": (-1, 0),
            "v": (0, 1),
            "^": (0, -1),
        }[mm[coord]]
        c = (coord[0]+dx, coord[1]+dy)
        adj = c
        if adj not in mm or mm[adj] == "#" or adj in visited:
            adjs = []
        else:
            adjs = [c]
    
    jj = False
    if len(adjs) >= 2:
        jj = True
    
    for a in adjs:
        traverse(mm, a, distance+1, visited.copy(), end_coord=end_coord)

def run(fname):
    lines = [line for line in open(fname, 'r').readlines()]

    mm = {}
    global max_x, max_y
    max_x = max_y = 0
    start_pos = end_pos = None

    for y, row in enumerate(lines):
        for x, val in enumerate(row.strip()):
            if val == "." and y == 0:
                start_pos = (x, y)
            if val == "." and y == len(lines)-1:
                end_pos = (x, y)
            mm[x, y] = val
            max_x = x
        max_y = y
    
    global DP
    DP = {}
    traverse(mm, start_pos)
    part1 = DP[end_pos]

    for k in mm:
        if mm[k] in "v^><":
            mm[k] = "."
    
    DP = {}
    traverse(mm, start_pos, end_coord=end_pos)
    part2 = DP[end_pos]

    print(f"part 1:")
    print(f"{part1}")

    print(f"part 2:")
    print(f"{part2}")

print("TEST")
run('inputs/test.txt')
print()
print("REAL")
run('inputs/day23.txt')