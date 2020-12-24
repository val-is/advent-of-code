from toolbox import memoize

inputs = [i.strip() for i in open("inputs/day24.txt", 'r').readlines()]

deltas = {
    "e":    (-1, 1),
    "ne":   (-1, 0),
    "nw":   (0, -1),
    "w":    (1, -1),
    "sw":   (1, 0),
    "se":   (0, 1)
}

def get_position(line):
    x = y = 0
    dgram = ""
    for i in line:
        if i in ["e", "w"] and dgram == "":
            dx, dy = deltas[i]
        elif dgram != "":
            dx, dy = deltas[dgram+i]
            dgram = ""
        else:
            dgram += i
            continue
        x += dx; y += dy
    return x, y

tiles_flipped = [*map(get_position, inputs)]
black_tiles = {tile for tile in tiles_flipped if tiles_flipped.count(tile) % 2 == 1}
part1 = len(black_tiles)
print(f"part 1: {part1}")

def neighbors(pos):
    x, y = pos
    return [(x+dx, y+dy) for dx, dy in deltas.values()]

def iterate_day(black):
    tiles_adj = {}
    for tile in black:
        for neighbor in neighbors(tile):
            tiles_adj[neighbor] = tiles_adj.get(neighbor, 0) + 1
    
    new_black = set()
    for tile in tiles_adj:
        if tile in black and (1 <= tiles_adj[tile] <= 2):
            new_black.add(tile)
        elif tile not in black and (tiles_adj[tile] == 2):
            new_black.add(tile)
    return new_black

tiles = black_tiles.copy()
for _ in range(100):
    tiles = iterate_day(tiles)
part2 = len(tiles)
print(f"part 2: {part2}")