inputs = [i.strip() for i in open('inputs/day11.txt', 'r').readlines()]

EMPTY = 0
OCCUPIED = 1
FLOOR = 2

seatMap = {}

for y, row in enumerate(inputs):
    for x, val in enumerate(row):
        v = FLOOR
        if val == ".":
            v = FLOOR
        if val == "#":
            v = OCCUPIED
        if val == "L":
            v = EMPTY
        seatMap[(x, y)] = v

mX, mY = 0, 0
for k in seatMap:
    mX = max(k[0], mX)
    mY = max(k[1], mY)
mX += 1
mY += 1

def print_map(mapIn):
    mX, mY = 0, 0
    for k in mapIn:
        mX = max(k[0], mX)
        mY = max(k[1], mY)
    for y in range(mY+1):
        s = ""
        for x in range(mX+1):
            v = mapIn[(x, y)]
            if v == FLOOR:
                s += "."
            if v == OCCUPIED:
                s += "#"
            if v == EMPTY:
                s += "L"
        print(s)

def get_occupied_adjacent(mapIn, x, y):
    s = 0
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            if dx == 0 and dy == 0:
                continue
            # if (x+dx, y+dy) not in mapIn:
            #     continue
            v = mapIn.get((x + dx, y + dy), EMPTY)
            if v == OCCUPIED:
                s += 1
    return s

def copyMap(mapIn):
    newMap = {}
    for key in mapIn:
        newMap[(key[0], key[1])] = mapIn[(key[0], key[1])]
    return newMap

def compareMap(a, b):
    diff = True
    for key in a:
        if a[key] != b[key]:
            diff = False
            break
    return diff

def count_occupied(mapIn):
    s = 0
    for seat in mapIn:
        if mapIn[seat] == OCCUPIED:
            s += 1
    return s

def run_generation(mapIn):
    newGen = copyMap(mapIn)
    for seat in mapIn:
        adj = get_occupied_adjacent(mapIn, seat[0], seat[1])
        if mapIn[seat] == EMPTY:
            if adj == 0:
                newGen[seat] = OCCUPIED
        if mapIn[seat] == OCCUPIED:
            if adj >= 4:
                newGen[seat] = EMPTY
    return newGen

# done = False
# curMap = copyMap(seatMap)
# while not done:
#     # print_map(curMap)
#     # print(count_occupied(curMap))
#     # print("\n\n")
#     newMap = run_generation(curMap)
#     if compareMap(newMap, curMap):
#         done = True
#         break
#     else:
#         curMap = newMap


# curMap = copyMap(seatMap)
# curMap = run_generation(curMap)
# curMap = run_generation(curMap)
# curMap[(1, 1)] = FLOOR
# print(get_occupied_adjacent(curMap, 1, 1))
# print_map(curMap)
# print("\n\n")

# part1 = count_occupied(newMap)
# print(f"Part 1: {part1}")

def get_occupied_adjacent_p2(mapIn, x, y):
    s = 0
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            if dx == 0 and dy == 0:
                continue
            for t in range(1, 1000):
                if (x+dx*t, y+dy*t) not in mapIn:
                    break
                v = mapIn.get((x + dx*t, y + dy*t), EMPTY)
                if v == OCCUPIED:
                    s += 1
                if v != FLOOR:
                    break
    return s

def run_generation_p2(mapIn):
    newGen = copyMap(mapIn)
    for seat in mapIn:
        adj = get_occupied_adjacent_p2(mapIn, seat[0], seat[1])
        # print(adj)
        if mapIn[seat] == EMPTY:
            if adj == 0:
                newGen[seat] = OCCUPIED
        if mapIn[seat] == OCCUPIED:
            if adj >= 5:
                newGen[seat] = EMPTY
    return newGen

# curMap = copyMap(seatMap)
# curMap = run_generation_p2(curMap)
# curMap = run_generation_p2(curMap)
# print_map(curMap)

done = False
curMap = copyMap(seatMap)
while not done:
    # print_map(curMap)
    # print(count_occupied(curMap))
    # print("\n\n")
    newMap = run_generation_p2(curMap)
    if compareMap(newMap, curMap):
        done = True
        break
    else:
        curMap = newMap

part2 = count_occupied(newMap)
print(f"Part 2: {part2}")