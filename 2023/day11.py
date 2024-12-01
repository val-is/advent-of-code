def get_max(mapping):
    max_x = 0
    max_y = 0
    for coord in mapping:
        max_x = max(max_x, coord[0])
        max_y = max(max_y, coord[1])
    return max_x, max_y

def add_row(mapping, row_idx):
    max_x, max_y = get_max(mapping)
    for y in range(row_idx, max_y+1)[::-1]:
        for x in range(max_x+1):
            mapping[x, y+1] = mapping[x, y]
    for x in range(max_x+1):
        mapping[x, row_idx] = False
    return mapping

def add_col(mapping, col_idx):
    max_x, max_y = get_max(mapping)
    for x in range(col_idx, max_x+1)[::-1]:
        for y in range(max_y+1):
            mapping[x+1, y] = mapping[x, y]
    for y in range(max_y+1):
        mapping[col_idx, y] = False
    return mapping

def get_dist(mapping, coord, target, empty_rows, empty_cols):
    mh = abs(coord[0]-target[0]) + abs(coord[1]-target[1])
    for row in empty_rows:
        if min(coord[1], target[1]) <= row <= max(coord[1], target[1]):
            mh += 1_000_000-1
    for col in empty_cols:
        if min(coord[0], target[0]) <= col <= max(coord[0], target[0]):
            mh += 1_000_000-1
    return mh

def render(mapping):
    max_x, max_y = get_max(mapping)
    for y in range(max_y+1):
        for x in range(max_x+1):
            print("#" if mapping[x, y] else ".", end="")
        print()
    print()

def run(fname):
    lines = [i.strip() for i in open(fname, 'r').readlines()]
    max_x = 0
    max_y = 0
    raw = {}
    for y, row in enumerate(lines):
        max_y = max(y, max_y)
        for x, val in enumerate(row.strip()):
            raw[x,y] = True if val == "#" else False
            max_x = max(x, max_x)
    
    empty_rows = []
    empty_cols = []
    for y in range(max_y+1):
        empty = True
        for x in range(max_x+1):
            if raw[x, y]:
                empty = False
                break
        if empty:
            empty_rows.append(y)
    # for offset, row in enumerate(empty_rows):
    #     raw = add_row(raw, row+offset)
    
    for x in range(max_x+1):
        empty = True
        for y in range(max_y+1):
            if raw[x, y]:
                empty = False
                break
        if empty:
            empty_cols.append(x)

    # for offset, col in enumerate(empty_cols):
    #     raw = add_col(raw, col+offset)
    # render(raw)
    
    galaxy_coords = []
    for coord in raw:
        if raw[coord]:
            galaxy_coords.append(coord)

    distances = {}
    for a in galaxy_coords:
        for b in galaxy_coords:
            if a == b:
                continue
            # if (b, a) in distances:
            #     continue
            distances[a, b] = get_dist(raw, a, b, empty_rows, empty_cols)
    
    # find MST
    part1 = 0
    for a in galaxy_coords:
        for b in galaxy_coords:
            if a == b:
                continue
            part1 += distances[a, b]
    # print(distances[(3, 0), (7, 8)])
    part1 //= 2
    # connected = []
    # paths_added = []
    # while not (len(connected) == 1 and len(connected[0]) == len(galaxy_coords)):
    #     shortest_pairing = None
    #     for pair in distances:
    #         if pair in paths_added:
    #             continue
    #         if shortest_pairing == None:
    #             shortest_pairing = pair
    #             continue
    #         if distances[pair] <= distances[shortest_pairing]:
    #             shortest_pairing = pair
    #     paths_added.append(shortest_pairing)
    #     part1 += distances[shortest_pairing]
    #     group_a = None
    #     group_b = None
    #     present = False
    #     for k, c in enumerate(connected):
    #         if (shortest_pairing[0] in c) and (shortest_pairing[1] in c):
    #             present = True
    #             break
    #         elif shortest_pairing[0] in c:
    #             group_a = k
    #             continue
    #         elif shortest_pairing[1] in c:
    #             group_b = k
    #             continue
    #     if group_a != None and group_b != None:
    #         connected[group_a] |= connected[group_b]
    #         del connected[group_b]
    #     if group_a != None and group_b == None:
    #         connected[group_a] |= set(shortest_pairing)
    #     if group_a == None and group_b != None:
    #         connected[group_b] |= set(shortest_pairing)
    #     if group_a == None and group_b == None and not present:
    #         connected.append(set(shortest_pairing))
    # print(paths_added)
    
    part2 = 0

    print(f"part 1:")
    print(f"{part1}")

    print(f"part 2:")
    print(f"{part2}")

print("TEST")
run('inputs/test.txt')
print()
print("REAL")
run('inputs/day11.txt')