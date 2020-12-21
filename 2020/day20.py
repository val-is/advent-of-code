from toolbox import memoize_the_world

tiles_raw = open("inputs/day20.txt", 'r').read().split("\n\n")

tiles = {}
for tile in tiles_raw:
    tile_id, data = tile.split("\n", 1)
    tile_id = int(tile_id.split(" ")[1][:-1])

    active = set()
    for y, line in enumerate(data.split("\n")):
        for x, val in enumerate(line.strip()):
            if val == "#":
                active.add((x, y))
    tiles[tile_id] = active

def apply_tile_transformation(func, tile):
    new_tiles = set()
    for active in tile:
        new_tiles.add(func(active))
    return new_tiles

def rotate_point(point, tile_width=10):
    x, y = point
    x, y = (x-tile_width//2, y-tile_width//2)
    x, y = y, -x
    return (x+tile_width//2, y+tile_width//2-1)

def flip_point_horiz(point, tile_width=10):
    x, y = point
    x = (tile_width-1) - x
    return (x, y)

def flip_point_vert(point, tile_height=10):
    x, y = point
    y = (tile_height-1) - y
    return (x, y)

rotate_tile_ccw = lambda tile: apply_tile_transformation(lambda x: rotate_point(x, 10), tile)
flip_tile_horiz = lambda tile: apply_tile_transformation(lambda x: flip_point_horiz(x, 10), tile)
flip_tile_vert  = lambda tile: apply_tile_transformation(lambda x: flip_point_vert(x, 10), tile)

def print_tile(tile, row=-1, col=-1):
    maxX, maxY = 0, 0
    for active in tile:
        x, y = active
        maxX, maxY = max(maxX, x), max(maxY, y)
    for y in range(maxY+1):
        s = ""
        for x in range(maxX+1):
            if row != -1 and y != row:
                continue
            if col != -1 and x != col:
                continue

            if (x, y) in tile:
                s += "#"
            else:
                s += "."
        print(s)

# calculate adjacencies
TOP, BOTTOM, LEFT, RIGHT = range(4)

def get_tile_side(tile, side, tile_size=10):
    assert side in [TOP, BOTTOM, RIGHT, LEFT]
    if side == TOP:
        return {point for point in tile if point[1] == 0}
    if side == BOTTOM:
        return {point for point in tile if point[1] == tile_size-1}
    if side == LEFT:
        return {point for point in tile if point[0] == 0}
    if side == RIGHT:
        return {point for point in tile if point[0] == tile_size-1}

def get_all_tile_sides(tile, tile_size=10):
    sides = {}
    for side in [TOP, BOTTOM, LEFT, RIGHT]:
        sides[side] = get_tile_side(tile, side, tile_size)
    return sides

# adjacency check w/out permutations
adj_cache = {}
def check_adjacent(tile_a, tile_b, tile_b_relative=None):
    key = (frozenset(tile_a), frozenset(tile_b), tile_b_relative)
    if key in adj_cache:
        return adj_cache[key]
    
    tile_a_sides, tile_b_sides = [get_all_tile_sides(i) for i in [tile_a, tile_b]]
    if tile_b_relative == None:
        for side_a in tile_a_sides:
            if tile_a_sides[side_a] in tile_b_sides.values():
                adj_cache[key] = True
                return True
    else:
        if tile_a_sides[tile_b_relative] in tile_b_sides.values():
            adj_cache[key] = True
            return True
    adj_cache[key] = False
    return False

def transform_tile(tile, ccw_rotations, flip_horiz, flip_vert):
    tile_permuted = tile.copy()
    for _ in range(ccw_rotations):
        tile_permuted = rotate_tile_ccw(tile_permuted)
    if flip_horiz:
        tile_permuted = flip_tile_horiz(tile_permuted)
    if flip_vert:
        tile_permuted = flip_tile_vert(tile_permuted)
    return tile_permuted

all_orientations = set(range(0b1111 + 1))

def get_id_from_orientation(ccw_rotations, flip_horiz, flip_vert):
    return ccw_rotations + 0b100 * (1 if flip_horiz else 0) + 0b1000 * (1 if flip_vert else 0)

def get_orientation_from_id(orientation_id):
    ccw_rotations = orientation_id & 0b11
    flip_horiz = orientation_id & 0b100 != 0
    flip_vert = orientation_id & 0b1000 != 0
    return (ccw_rotations, flip_horiz, flip_vert)

def transform_tile_orientation_id(tile, orientation_id):
    ccw, horiz, vert = get_orientation_from_id(orientation_id)
    return transform_tile(tile, ccw, horiz, vert)

transformed_tiles = {}
for tile_id in tiles:
    orientations = {}
    for orientation_id in all_orientations:
        orientations[orientation_id] = frozenset(transform_tile_orientation_id(tiles[tile_id].copy(), orientation_id))
    transformed_tiles[tile_id] = orientations

# adjacency check with transformations. returns set of valid orientations
def check_adjacent_id(tile_id_a, tile_id_b, tile_b_relative=None):
    valid_orientations = set()
    for transformation_a in transformed_tiles[tile_id_a]:
        for transformation_b in transformed_tiles[tile_id_b]:
            if check_adjacent(transformed_tiles[tile_id_a][transformation_a],
            transformed_tiles[tile_id_b][transformation_b], tile_b_relative):
                valid_orientations.add(transformation_a)
    return valid_orientations

adjacencies = {}
for tile_id in tiles:
    neighbors = set()
    for other_id in tiles:
        if other_id == tile_id:
            continue
        orientations = check_adjacent_id(tile_id, other_id)
        if len(orientations) != 0:
            neighbors.add(other_id)
    adjacencies[tile_id] = neighbors

# part 1 solving. just count number of corners
corners = set()
for tile_id in adjacencies:
    if len(adjacencies[tile_id]) == 2:
        corners.add(tile_id)
assert len(corners) == 4
acc = 1
for tile_id in corners:
    acc *= tile_id
print(f"part 1: {acc}")

# build grid
top_left_id = corners.pop()
tile_grid = {(0, 0): top_left_id} # (x, y): tile_id

grid_size = 12 # TODO update if not on testing data

for y in range(0, grid_size):
    for x in range(0, grid_size):
        if x == y == 0:
            continue
        target_adj = 4
        if x in [0, grid_size-1] or y in [0, grid_size-1]:
            target_adj = 3
        if x in [0, grid_size-1] and y in [0, grid_size-1]:
            target_adj = 2
        above_tile = left_tile = None
        if x != 0: # not left side
            left_tile = tile_grid[(x-1, y)]
        if y != 0: # not top row
            above_tile = tile_grid[(x, y-1)]
        # find common adjacencies between left and above tile
        # A.
        # .B
        # returns two tiles, A and B. we can throw out one that's already been used to get B
        above_adj = adjacencies.get(above_tile, None)
        left_adj = adjacencies.get(left_tile, None)
        adj = set()
        if above_adj == None:
            adj = left_adj
        elif left_adj == None:
            adj = above_adj
        else:
            adj = left_adj.intersection(above_adj)
        # throw out tiles already in grid
        tiles_present = set(tile_grid.values())
        adj = adj - tiles_present
        adj_target = set()
        for i in adj:
            if len(adjacencies[i]) == target_adj:
                adj_target.add(i)
        tile_grid[(x, y)] = adj_target.pop()

orientations = {}
for y in range(0, grid_size):
    for x in range(0, grid_size):
        get_tile = lambda dx, dy: tile_grid[(x+dx, y+dy)]
        tile = get_tile(0, 0)
        valid_orientations = all_orientations.copy()
        if x != 0:
            valid_orientations.intersection_update(check_adjacent_id(tile, get_tile(-1, 0), LEFT))
        if x != grid_size-1:
            valid_orientations.intersection_update(check_adjacent_id(tile, get_tile(1, 0), RIGHT))
        if y != 0:
            valid_orientations.intersection_update(check_adjacent_id(tile, get_tile(0, -1), TOP))
        if y != grid_size-1:
            valid_orientations.intersection_update(check_adjacent_id(tile, get_tile(0, 1), BOTTOM))
        
        assert len(valid_orientations) == 2 # 2 possible ways to get to any orientation via/ rotate/flip
        orientations[(x, y)] = valid_orientations.pop()

total_grid = set()
for tile in tile_grid:
    tx, ty = tile
    tile_id = tile_grid[tile]
    orientation = orientations[tile]
    tile_transformed = transform_tile_orientation_id(tiles[tile_id], orientation)
    for t in tile_transformed:
        x, y = t
        if x in [0, 9] or y in [0, 9]:
            continue
        total_grid.add(((x-1) + tx*8, (y-1)+ ty*8))

rotate_grid_ccw = lambda tile: apply_tile_transformation(lambda x: rotate_point(x, 8*grid_size), tile)
flip_grid_horiz = lambda tile: apply_tile_transformation(lambda x: flip_point_horiz(x, 8*grid_size), tile)
flip_grid_vert  = lambda tile: apply_tile_transformation(lambda x: flip_point_vert(x, 8*grid_size), tile)

def check_monster_pos(grid, monster, pos_x, pos_y):
    for tile in monster:
        x, y = tile
        if (x + pos_x, y + pos_y) not in grid:
            return False
    return True

monster_raw = ["                  #", "#    ##    ##    ###", " #  #  #  #  #  #   "]
monster = set()
for y, line in enumerate(monster_raw):
    for x, v in enumerate(line):
        if v == "#":
            monster.add((x, y))

def find_monster(grid):
    grid_w, grid_h = 0, 0
    for tile in grid:
        x, y = tile
        grid_w, grid_h = max(x, grid_w), max(y, grid_h)
    monsters = 0
    for x in range(grid_w+1):
        for y in range(grid_h+1):
            if check_monster_pos(grid, monster, x, y):
                monsters += 1
    return monsters

max_monsters = 0
for ccw in range(4):
    for flipV in [True, False]:
        for flipH in [True, False]:
            transformed = total_grid.copy()
            for _ in range(ccw):
                transformed = rotate_grid_ccw(transformed)
            if flipV:
                transformed = flip_grid_vert(transformed)
            if flipH:
                transformed = flip_grid_horiz(transformed)
            max_monsters = max(find_monster(transformed), max_monsters)

part2 = len(total_grid) - max_monsters * len(monster)
print(f"Part 2: {part2}")