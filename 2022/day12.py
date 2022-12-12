import sys
sys.setrecursionlimit(10000) # gaming

inputs = [i.strip() for i in open('inputs/day12.txt', 'r').readlines()]

def conv_elevation(ch):
    return 'abcdefghijklmnopqrstuvwxyz'.index(ch)

tiles = {}
start_pos = end_pos = ()
for y, row in enumerate(inputs):
    for x, val in enumerate(row.strip()):
        pos = (x, y)
        if val == 'S':
            start_pos = pos
            tiles[pos] = conv_elevation('a')
        elif val == 'E':
            end_pos = pos
            tiles[pos] = conv_elevation('z')
        else:
            tiles[pos] = conv_elevation(val)

def get_adj(tiles, pos):
    adj = [
        (pos[0]+1, pos[1]),
        (pos[0]-1, pos[1]),
        (pos[0], pos[1]+1),
        (pos[0], pos[1]-1),
    ]
    return [i for i in adj if i in tiles]

def can_move_to(tiles, fro, to):
    d_h = tiles[fro] - tiles[to]
    if -1 <= d_h <= 999:
        return True
    return False

def score_tile(pos):
    return abs(pos[0] - end_pos[0]) + abs(pos[1] - end_pos[1])

next_tiles = [start_pos]
best_dists = {start_pos: -1}

while len(next_tiles) > 0:
    cur_pos = next_tiles.pop(0)
    cur_dist = best_dists[cur_pos]
    for adj in get_adj(tiles, cur_pos):
        if not can_move_to(tiles, cur_pos, adj):
            continue
        dist = cur_dist + 1
        if adj in best_dists and best_dists[adj] <= dist:
            continue
        best_dists[adj] = dist
        if adj in next_tiles:
            continue
        next_tiles.append(adj)

    # next_tiles = sorted(next_tiles, key=score_tile)

# def trav_recurse(tiles, cur_pos, cur_dist=0, best_dists={}, travelled=[]):
#     if cur_pos == end_pos:
#         return
#     if cur_pos in travelled:
#         return
#     adjs = get_adj(tiles, cur_pos)
#     adjs = sorted(adjs, key=lambda x: tiles[x])[::-1]
#     new_travelled = [*travelled] + [cur_pos]
#     for adj in adjs:
#         if not can_move_to(tiles, cur_pos, adj):
#             continue

#         if adj in best_dists:
#             if cur_dist >= best_dists[adj]:
#                 continue
        
#         best_dists[adj] = cur_dist
#         trav_recurse(tiles, adj, cur_dist+1, best_dists, new_travelled)
#     return best_dists

# best_dists = {}
# trav_recurse(tiles, start_pos, 0, best_dists)
part1 = best_dists[end_pos]+1
print(f"part 1: {part1}")

next_tiles = [i for i in tiles if tiles[i] == 0]
while len(next_tiles) > 0:
    cur_pos = next_tiles.pop(0)
    cur_dist = best_dists[cur_pos]
    if tiles[cur_pos] == 0:
        cur_dist = -1
    for adj in get_adj(tiles, cur_pos):
        if not can_move_to(tiles, cur_pos, adj):
            continue
        dist = cur_dist + 1
        if adj in best_dists and best_dists[adj] <= dist:
            continue
        best_dists[adj] = dist
        if adj in next_tiles:
            continue
        next_tiles.append(adj)

# for pos in tiles:
#     if tiles[pos] == 0:
#         trav_recurse(tiles, pos, 0, best_dists)

part2 = best_dists[end_pos]+1
print(f"part 2: {part2}")