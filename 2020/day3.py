inputs = [i.strip() for i in open('inputs/day3.txt', 'r').readlines()]

tree_locs = set()
board_x, board_y = 0, 0
for y, row in enumerate(inputs):
    for x, val in enumerate(row):
        if val == "#":
            tree_locs.add((x, y))
        board_x = max(x, board_x)
    board_y = max(y, board_y)
board_x += 1
board_y += 1

def calc_trees(start, slope):
    dx, dy = slope
    x, y = start
    x += dx
    y += dy
    tree_count = 0
    while y < board_y:
        if (x, y) in tree_locs:
            tree_count += 1
        x = ((x + dx) % board_x)
        y += dy
    return tree_count

part1 = calc_trees((0, 0), (3, 1))
print(f"part 1: {part1}")

slopes = [
    (1, 1),
    (3, 1),
    (5, 1),
    (7, 1),
    (1, 2)
]
part2 = 1
for s in slopes:
    part2 *= calc_trees((0, 0), s)
print(f"part 2: {part2}")
