right = 0
left = 1
up = 2
down = 3

def get_tile_in_line(pos, direction):
    dx, dy = {
        right: (1, 0),
        left: (-1, 0),
        up: (0, -1),
        down: (0, 1),
    }[direction]
    return (pos[0]+dx, pos[1]+dy)

cached = set()
def get_next_beams(m, pos, direction):
    global cached
    next_tile = get_tile_in_line(pos, direction)
    if (pos, direction) in cached:
        return []
    cached.add((pos, direction))
    if next_tile not in m:
        return []
    if m[next_tile] == ".":
        return [(next_tile, direction)]
    if m[next_tile] == "/":
        if direction == left:
            return [(next_tile, down)]
        if direction == up:
            return [(next_tile, right)]
        if direction == right:
            return [(next_tile, up)]
        if direction == down:
            return [(next_tile, left)]
    if m[next_tile] == "\\":
        if direction == left:
            return [(next_tile, up)]
        if direction == up:
            return [(next_tile, left)]
        if direction == right:
            return [(next_tile, down)]
        if direction == down:
            return [(next_tile, right)]
    if m[next_tile] == "|":
        if direction == right or direction == left:
            return [(next_tile, up), (next_tile, down)]
        else:
            return [(next_tile, direction)]
    if m[next_tile] == "-":
        if direction == up or direction == down:
            return [(next_tile, left), (next_tile, right)]
        else:
            return [(next_tile, direction)]
    assert False

def eval_start(m, beam_start):
    global cached
    energized = set()
    cached = set()
    beams = [beam_start]
    energized.add(beams[0][0])

    while len(beams) > 0:
        next_beams = []
        for beam in beams:
            nnn = get_next_beams(m, beam[0], beam[1])
            next_beams.extend(nnn)
            for b in nnn:
                energized.add(b[0])
        beams = next_beams
    return len(energized)-1


def run(fname):
    global cached
    lines = [line for line in open(fname, 'r').readlines()]
    m = {}
    max_y = 0
    max_x = 0
    for y, row in enumerate(lines):
        max_y = y
        for x, val in enumerate(row.strip()):
            m[x, y] = val
            max_x = x
    part1 = eval_start(m, ((-1, 0), right))
    part2 = 0
    for x in range(max_x+1):
        part2 = max(part2, eval_start(m, ((x, -1), down)))
        part2 = max(part2, eval_start(m, ((x, max_y+1), up)))
    for y in range(max_y+1):
        part2 = max(part2, eval_start(m, ((-1, y), right)))
        part2 = max(part2, eval_start(m, ((max_x+1, y), left)))

    print(f"part 1:")
    print(f"{part1}")

    print(f"part 2:")
    print(f"{part2}")

print("TEST")
run('inputs/test.txt')
print()
print("REAL")
run('inputs/day16.txt')