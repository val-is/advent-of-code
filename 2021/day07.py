import numpy as np

inputs = [int(i) for i in open('inputs/day07.txt', 'r').read().strip().split(",")]

target = int(np.median(inputs))

s = 0
for i in inputs:
    s += abs(i - target)
part1 = s
print(f"part 1: {part1}")

def get_fuel_cts(crabs, pos):
    s = 0
    for i in crabs:
        dist = abs(pos - i)
        fuel_used = 0
        for j in range(dist+1):
            fuel_used += j
        s += fuel_used
    return s


# :PPPPPPPPP this is so dumb and slow but it works at least
smallest_dist = None
v = 0
for i in range(0, max(inputs)):
    fuel = get_fuel_cts(inputs, i)
    if smallest_dist == None or fuel < smallest_dist:
        smallest_dist = fuel
        v = i

part2 = smallest_dist
print(f"part 2: {part2}")
