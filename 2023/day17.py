import sys
# sys.setrecursionlimit()

left = 0
right = 1
up = 2
down = 3

def get_tile_dir(tile, direction):
    dx, dy = {
        left: (-1, 0),
        right: (1, 0),
        up: (0, -1),
        down: (0, 1),
    }[direction]
    return (tile[0]+dx, tile[1]+dy)

def manhat(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

# def render_grid(max_x, max_y, filled):
#     for y in range(max_y+1):
#         for x in range(max_x+1):
#             if (x, y) in filled:
#                 print("#", end="")
#             else:
#                 print(" ", end="")
#         print()
#     print()

# max_x = max_y = 0

# DP = {} # coord: (dist_to_target, prev_tiles, direction)
# stack = []
# def traverse(mm, coord, target, prev_tiles, direction, visited=set(), depth=0):
#     global stack
#     # print(coord, prev_tiles, direction)
#     # input()
#     # if depth > max_depth:
#     #     return 9999999999
#     if coord == target:
#         # render_grid(max_x, max_y, visited)
#         return mm[coord]
#     if coord in visited:
#         return 9999999999
    
#     dp_key = (coord, target, prev_tiles, direction)
#     if dp_key in DP:
#         return DP[dp_key]

#     next_directions = []
#     if direction in [left, right]:
#         next_directions = [up, down]
#     else:
#         next_directions = [left, right]
#     if prev_tiles <= 2:
#         next_directions.append(direction)
#     # print(direction in next_directions)
    
#     next_best = 999999999
#     adjs = [(get_tile_dir(coord, d), d) for d in next_directions]
#     # ranked = sorted(adjs, key=lambda x: manhat(x[0], target))
#     next_visited = visited | {(coord[0], coord[1])}
#     for rr in adjs:
#         adj, d = rr
#         if adj not in mm:
#             continue
#         if d != direction:
#             next_prev_tiles = 1
#         else:
#             next_prev_tiles = prev_tiles + 1
#         dist = traverse(mm, adj, target, next_prev_tiles, d, visited=next_visited, depth=depth+1)
#         next_best = min(next_best, dist)
    
#     val = next_best + mm[coord]
#     DP[dp_key] = val
#     return val

def run(fname):
    lines = [line for line in open(fname, 'r').readlines()]

    mm = {}
    global max_x
    global max_y
    global DP
    DP = {}
    # max_y = 0
    # max_x = 0
    for y, row in enumerate(lines):
        for x, val in enumerate(row.strip()):
            mm[x, y] = int(val)
            max_x = x
        max_y = y

    part1 = 0

    distances = {k: None for k in mm}
    start = {((0, 0), right, 1), ((0, 0), down, 1)}
    for k in start:
        distances[k] = 0
    visited = start
    node_stack = [*start]
    while len(node_stack) > 0:
        cur_node = node_stack.pop()
        cur_coord, cur_dir, cur_trav = cur_node
        possible_dir = []
        if cur_dir in [left, right]:
            possible_dir = [up, down]
        else:
            possible_dir = [left, right]
        if cur_trav <= 2:
            possible_dir.append(cur_dir)
        for next_direction in possible_dir:
            next_coord = get_tile_dir(cur_coord, next_direction)
            next_key = (next_coord, next_direction, 1 if next_direction != cur_dir else cur_trav+1)
            if next_key in visited:
                continue





    part2 = 0

    print(f"part 1:")
    print(f"{part1}")

    print(f"part 2:")
    print(f"{part2}")

print("TEST")
run('inputs/test.txt')
print()
print("REAL")
run('inputs/day17.txt')