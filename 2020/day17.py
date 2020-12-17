from toolbox import memoize_the_world, profile

inputs = [i.strip() for i in open("inputs/day17.txt", 'r').readlines()]

initial_alive = set()
for y, row in enumerate(inputs):
    for x, val in enumerate(row):
        if val == "#":
            initial_alive.add((x, y, 0, 0))

@memoize_the_world
def get_adj(coords, n_dims):
    deltas = [-1, 0, 1]
    x, y, z, w = coords
    adj = set()
    for dx in deltas:
        for dy in deltas:
            for dz in deltas:
                for dw in deltas:
                    if n_dims == 3:
                        dw = 0
                    if dx == dy == dz == dw == 0:
                        continue
                    adj.add((x+dx, y+dy, z+dz, w+dw))
    return adj

def run_cycle(alive, n_dims):
    new_alive = set()
    adjacencies = {}
    for alive_coords in alive:
        for adj_cell in get_adj(alive_coords, n_dims):
            if adj_cell not in adjacencies:
                adjacencies[adj_cell] = 1
                continue
            adjacencies[adj_cell] += 1
    for coords in adjacencies:
        val = adjacencies[coords]
        if coords in alive and val in [2, 3]:
            new_alive.add(coords)
        if coords not in alive and val in [3]:
            new_alive.add(coords)
    return new_alive

def run_generations(initial_alive, n_dims, generations=6):
    alive = initial_alive.copy()
    for _ in range(generations):
        alive = run_cycle(alive, n_dims)
    return len(alive)

part1 = run_generations(initial_alive, 3)
print(f"part 1: {part1}")

part2 = run_generations(initial_alive, 4)
print(f"part 2: {part2}")