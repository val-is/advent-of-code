import sys
sys.setrecursionlimit(10**6)

a = "#" # blocked
b = " " # floor
c = "." # squeeze

map_equivs = {
    ".": [
        [b, b, b],
        [b, b, b],
        [b, b, b],
    ],
    "|": [
        [c, a, c],
        [c, a, c],
        [c, a, c],
    ],
    "-": [
        [c, c, c],
        [a, a, a],
        [c, c, c],
    ],
    "7": [
        [c, c, c],
        [a, a, c],
        [c, a, c],
    ],
    "J": [
        [c, a, c],
        [a, a, c],
        [c, c, c],
    ],
    "F": [
        [c, c, c],
        [c, a, a],
        [c, a, c],
    ],
    "L": [
        [c, a, c],
        [c, a, a],
        [c, c, c],
    ],
    "S": [
        [c, a, c],
        [a, a, a],
        [c, a, c],
    ],
}

def generate_new_map(mapping):
    new_mapping = {}
    for coord in mapping:
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                new_mapping[coord[0]*3+dx+1, coord[1]*3+dy+1] = map_equivs[mapping[coord]][dy+1][dx+1]
    return new_mapping

def get_adj(mapping, coord, cur_tile):
    x, y = coord
    adj = []
    if cur_tile in "-LFS" and mapping.get((x+1, y), "A") in "-J7": # go right
        adj.append((x+1, y))
    if cur_tile in "-J7S" and mapping.get((x-1, y), "A") in "-LF": # go left
        adj.append((x-1, y))
    if cur_tile in "|F7S" and mapping.get((x, y+1), "A") in "|LJ": # go down
        adj.append((x, y+1))
    if cur_tile in "|LJS" and mapping.get((x, y-1), "A") in "|F7": # go up
        adj.append((x, y-1))
    return adj

def ggg(coord):
    x, y = coord
    adj = []
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            if dx == dy == 0:
                continue
            adj.append((x+dx, y+dy))
    return adj

max_x = 0
max_y = 0
def flood_fill(squeeze_mapping, coord, visited=set(), filled=set()):
    if len(visited) == 0:
        visited.add(coord)
        if squeeze_mapping[coord] == b:
            filled.add(coord)
    for adj in ggg(coord):
        if (not (0 <= adj[0] <= max_x)) or (not (0 <= adj[1] <= max_y)):
            visited.add(adj)
            continue
        if adj in visited:
            continue
        if squeeze_mapping[adj] == a:
            continue
        if squeeze_mapping[adj] == b:
            filled.add(adj)
        visited.add(adj)
        flood_fill(squeeze_mapping, adj, visited, filled)
    return visited, filled

c = 0
def get_connected(mapping, coord, visited=set(), connected_coords=set()):
    global c
    print(c)
    c += 1
    if len(visited) == 0:
        visited.add(coord)
        connected_coords.add(coord)
    for adj in get_adj(mapping, coord, mapping[coord]):
        if adj not in mapping:
            continue
        if adj in connected_coords or adj in visited:
            continue
        visited.add(adj)
        connected_coords.add(adj)
        get_connected(mapping, adj, visited, connected_coords)
        c-=1
    return connected_coords

def render(mapping):
    max_x = 0
    max_y = 0
    for k in mapping:
        max_x = max(max_x, k[0])
        max_y = max(max_y, k[1])
    for x in range(max_x+1):
        for y in range(max_y+1):
            print(mapping[x, y], end="")
        print()
    print()

def run(fname):
    lines = [i.strip() for i in open(fname, 'r').readlines()]

    mapping = {}
    start_coord = None
    for y, row in enumerate(lines):
        for x, val in enumerate(row.strip()):
            mapping[x, y] = val
            if val == "S":
                start_coord = (x, y)
    
    connected = get_connected(mapping, start_coord, set(), set())
    part1 = len(connected)/2

    updated_mapping = {k: mapping[k] for k in mapping}
    for i in updated_mapping:
        if i not in connected:
            updated_mapping[i] = "."
    squeeze_mapping = generate_new_map(updated_mapping)
    render(squeeze_mapping)

    global max_x, max_y
    max_x = 0
    max_y = 0
    for k in squeeze_mapping:
        max_x = max(max_x, k[0])
        max_y = max(max_y, k[1])
    visited, filled = flood_fill(squeeze_mapping, (0, 0), set(), set())
    outside_sum = len(filled)

    part2 = (len([i for i in squeeze_mapping if squeeze_mapping[i] == b]) - outside_sum) / 9

    print(f"part 1:")
    print(f"{part1}")

    print(f"part 2:")
    print(f"{part2}")

print("TEST")
run('inputs/test.txt')
print()
print("REAL")
run('inputs/day10.txt')