inputs = [tuple(map(int, i.strip().split(","))) for i in open("inputs/day18.txt", 'r').readlines()]

filled = {}
mi_bounds = [9999,9999,9999]
ma_bounds = [-9999,-9999,-9999]
for i in inputs:
    filled[i] = True
    for idx in range(3):
        mi_bounds[idx] = min(mi_bounds[idx], i[idx]-1)
        ma_bounds[idx] = max(ma_bounds[idx], i[idx]+1)

exposed_faces = 0
for block_coord in filled:
    x, y, z = block_coord
    for dx, dy, dz in [
        (-1, 0, 0),
        (1, 0, 0),
        (0, -1, 0),
        (0, 1, 0),
        (0, 0, -1),
        (0, 0, 1),
    ]:
        if (x+dx, y+dy, z+dz) not in filled:
            exposed_faces += 1
print(f"part 1: {exposed_faces}")

# part 2
# floodfill exterior to get air blocks
# compute exposed like before

tile_queue = [tuple(mi_bounds)]
visited = set()
exposed_faces = 0
while len(tile_queue) > 0:
    tile = tile_queue.pop(0)
    visited.add(tile)
    x, y, z = tile
    for dx, dy, dz in [
        (-1, 0, 0),
        (1, 0, 0),
        (0, -1, 0),
        (0, 1, 0),
        (0, 0, -1),
        (0, 0, 1),
    ]:
        adj_pos = (x+dx, y+dy, z+dz)
        if not ((mi_bounds[0] <= adj_pos[0] <= ma_bounds[0]) and 
                (mi_bounds[1] <= adj_pos[1] <= ma_bounds[1]) and 
                (mi_bounds[2] <= adj_pos[2] <= ma_bounds[2])):
            continue
        if adj_pos in filled:
            exposed_faces += 1
            continue
        if adj_pos in visited or adj_pos in tile_queue:
            continue
        tile_queue.append(adj_pos)
print(f"part 2: {exposed_faces}")