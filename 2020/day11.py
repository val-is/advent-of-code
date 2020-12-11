inputs = [i.strip() for i in open('inputs/day11.txt', 'r').readlines()]

EMPTY = 0
OCCUPIED = 1
FLOOR = 2

seatMap = {}

mX = mY = 0
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
        mX = x+1
    mY = y+1

def print_map(mapIn):
    for y in range(mY+1):
        s = ""
        for x in range(mX+1):
            s += {
                FLOOR: ".",
                OCCUPIED: "#",
                EMPTY: "L"
            }[mapIn[(x, y)]]
        print(s)

def copy_map(mapIn):
    newMap = {}
    for key in mapIn:
        newMap[key] = mapIn[key]
    return newMap

def compare_map(a, b):
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

def get_occupied_adjacent_p1(mapIn, x, y):
    s = 0
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            if dx == 0 and dy == 0:
                continue
            v = mapIn.get((x + dx, y + dy), EMPTY)
            if v == OCCUPIED:
                s += 1
    return s

def run_generation_p1(mapIn):
    newGen = copy_map(mapIn)
    for seat in mapIn:
        adj = get_occupied_adjacent_p1(mapIn, seat[0], seat[1])
        if mapIn[seat] == EMPTY and adj == 0:
            newGen[seat] = OCCUPIED
        if mapIn[seat] == OCCUPIED and adj >= 4:
            newGen[seat] = EMPTY
    return newGen

curMap = copy_map(seatMap)
while True:
    newMap = run_generation_p1(curMap)
    if compare_map(newMap, curMap):
        break
    curMap = newMap
part1 = count_occupied(newMap)
print(f"Part 1: {part1}")

def get_occupied_adjacent_p2(mapIn, x, y):
    s = 0
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            if dx == 0 and dy == 0:
                continue
            t = 0
            while (t := t + 1) > 0:
                if (x + dx*t, y + dy*t) not in mapIn:
                    break
                v = mapIn[(x + dx*t, y + dy*t)]
                if v == OCCUPIED:
                    s += 1
                if v != FLOOR:
                    break
    return s

def run_generation_p2(mapIn):
    newGen = copy_map(mapIn)
    for seat in mapIn:
        adj = get_occupied_adjacent_p2(mapIn, seat[0], seat[1])
        if mapIn[seat] == EMPTY and adj == 0:
            newGen[seat] = OCCUPIED
        if mapIn[seat] == OCCUPIED and adj >= 5:
            newGen[seat] = EMPTY
    return newGen

curMap = copy_map(seatMap)
while True:
    newMap = run_generation_p2(curMap)
    if compare_map(newMap, curMap):
        break
    curMap = newMap
part2 = count_occupied(newMap)
print(f"Part 2: {part2}")