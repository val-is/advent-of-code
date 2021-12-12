inputs = open('inputs/day11.txt', 'r').readlines()

initial_octopi = {}
for y, row in enumerate(inputs):
    for x, val in enumerate(row.strip()):
        val = int(val)
        initial_octopi[(x, y)] = val

def get_adj(coord, octopi):
    return {i for i in [
        (coord[0]+1, coord[1]),
        (coord[0]-1, coord[1]),
        (coord[0], coord[1]+1),
        (coord[0], coord[1]-1),
        (coord[0]+1, coord[1]+1),
        (coord[0]+1, coord[1]-1),
        (coord[0]-1, coord[1]+1),
        (coord[0]-1, coord[1]-1),
        ] if i in octopi}

part1 = 0
all_flashed = False
def step(octopi):
    global part1
    global all_flashed
    updated = {}
    flashed = set()
    confirmed_flash = False

    for i in octopi:
        updated[i] = octopi[i] + 1

    while True:
        for coord in updated:
            v = updated[coord]
            if v > 9 and coord not in flashed:
                adj = get_adj(coord, updated)
                for a in adj:
                    updated[a] += 1
                part1 += 1
                confirmed_flash = True
                flashed.add(coord)
                break

        if not confirmed_flash:
            break
        else:
            confirmed_flash = False

    for v in flashed:
        updated[v] = 0

    all = True
    for k in updated:
        if k not in flashed:
            all = False
    if all:
        all_flashed = True

    return updated

def get_bounds(o):
    m_x, m_y = 0, 0
    for k in o:
        m_x = max(m_x, k[0])
        m_y = max(m_y, k[1])
    return m_x, m_y

def printgrid(octopi):
    m_x, m_y = get_bounds(octopi)
    for row in range(m_y+1):
        s = ""
        for col in range(m_x+1):
            s += str(octopi[(col, row)])
        print(s)
    print("")

# octopi = initial_octopi
# for _ in range(100):
#     octopi = step(octopi)

# printgrid(octopi)

print(f"part 1: {part1}")

steps = 0
octopi = initial_octopi
while not all_flashed:
    octopi = step(octopi)
    steps += 1

part2 = steps
print(f"part 2: {part2}")
