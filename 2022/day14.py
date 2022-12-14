inputs = [i.strip() for i in open('inputs/day14.txt', 'r').readlines()]

tiles = set()
highest_y = 0
for line in inputs:
    coords = line.split(' -> ')
    cur_coords = None
    for coord in coords:
        a, b = [int(i) for i in coord.strip().split(",")]
        if cur_coords == None:
            cur_coords = (a, b)
        else:
            xs = sorted([a, cur_coords[0]])
            ys = sorted([b, cur_coords[1]])
            highest_y = max(ys[1], highest_y)
            for x in range(xs[0], xs[1]+1):
                for y in range(ys[0], ys[1]+1):
                    tiles.add((x, y))
            cur_coords = (a, b)

sand_source = (500, 0)

def sim_new_sand(tiles, cur_sand, source=sand_source, floor=-1):
    cur_pos = sand_source
    while True:
        if cur_pos[1] > highest_y+1:
            return True
        # attempt to move
        attempted_locations = [
            (cur_pos[0], cur_pos[1]+1),
            (cur_pos[0]-1, cur_pos[1]+1),
            (cur_pos[0]+1, cur_pos[1]+1),
        ]
        moved = False
        for location in attempted_locations:
            if floor != -1 and location[1] == floor:
                continue
            elif location in tiles or location in cur_sand:
                continue
            else:
                moved = True
                cur_pos = location
                break
        if not moved:
            return cur_pos

sand_tiles = set()
done = False
while not done:
    result = sim_new_sand(tiles, sand_tiles, sand_source)
    if result == True:
        done = True
        break
    sand_tiles.add(result)

part1 = len(sand_tiles)
print(f"part 1: {part1}")

sand_tiles = set()
done = False
while not done:
    if result == sand_source:
        done = True
        break
    result = sim_new_sand(tiles, sand_tiles, sand_source, floor=highest_y+2)
    if result == True:
        done = True
        break
    sand_tiles.add(result)

part2 = len(sand_tiles)
print(f"part 2: {part2}")