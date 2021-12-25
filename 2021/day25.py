inputs = open('inputs/day25.txt', 'r').readlines()

east = set()
south = set()

m_x, m_y = 0, 0

for y, row in enumerate(inputs):
    for x, val in enumerate(row.strip()):
        if val == "v":
            south.add((x,y))
        elif val == ">":
            east.add((x,y))
        m_x = max(x+1, m_x)
    m_y = max(y+1, m_y)

def wrap_coord(c):
    x, y = c
    if x >= m_x:
        x = 0
    if y >= m_y:
        y = 0
    return (x, y)

def do_step(east, south):
    n_east = set()
    n_south = set()

    for cuc in east:
        x, y = cuc
        n = (x+1, y)
        n = wrap_coord(n)
        if n in east or n in south:
            n_east.add(cuc)
        else:
            n_east.add(n)
    for cuc in south:
        x, y = cuc
        n = (x, y+1)
        n = wrap_coord(n)
        if n in n_east or n in south:
            n_south.add(cuc)
        else:
            n_south.add(n)
    return n_east, n_south

step = 1
while True:
    n_east, n_south = do_step(east, south)
    if len(east) == len(n_east & east) and len(south) == len(n_south & south):
        break
    east = n_east
    south = n_south
    step += 1

part1 = step
print(f"part 1: {part1}")

print(f"no part 2. ggs!")
