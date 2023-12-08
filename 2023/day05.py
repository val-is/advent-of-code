# lines = [i.strip() for i in open('inputs/day05.txt', 'r').readlines()]

# def get_overlapping_range(a1, a2, b1, b2):
#     lhs = max(a1, b1)
#     rhs = min(a2, b2)
#     if lhs > rhs:
#         return None
#     return lhs, rhs

# seeds = []

# for seed in lines[0].split(": ")[1].split(" "):
#     seeds.append(int(seed))

# seed_to_lowest = []

# maps = []
# on_map = False
# ranges = []
# for line in lines:
#     if "map" in line:
#         on_map = True
#         maps.append(dict())
#     elif len(line) == 0 and on_map:
#         on_map = False

#         next_seeds = []
#         for seed in seeds:
#             added = False
#             for b_start in maps[-1]:
#                 a_start, ran = maps[-1][b_start]
#                 if a_start <= seed <= a_start + ran:
#                     next_seeds.append(seed + (b_start - a_start))
#                     added = True
#                     break
#             if not added:
#                 next_seeds.append(seed)
#         seeds = next_seeds
    
#     if on_map and "map" not in line:
#         k, start, rang = [*map(int, line.split(" "))]
#         maps[-1][k] = (start, rang)

# part1 = min(seeds)
# part2 = 0

# print(f"part 1:")
# print(f"{part1}")

# print(f"part 2:")
# print(f"{part2}")



lines = [i.strip() for i in open('inputs/day05.txt', 'r').readlines()]

def get_overlapping_range(a1, a2, b1, b2):
    lhs = max(a1, b1)
    rhs = min(a2, b2)
    if lhs > rhs:
        return None
    return lhs, rhs

seeds = []
a = None
for seed in lines[0].split(": ")[1].split(" "):
    if a == None:
        a = int(seed)
    else:
        seeds.append([a, a+int(seed)])
        a = None

seed_to_lowest = []

maps = []
on_map = False
ranges = []
for line in lines:
    if "map" in line:
        on_map = True
        maps.append(dict())
    elif len(line) == 0 and on_map:
        on_map = False

        next_seeds = []
        for seed in seeds:
            ranges_added = []
            for dest_start in maps[-1]:
                source_start, ran = maps[-1][dest_start]
                overlap = get_overlapping_range(*seed, source_start, source_start+ran)
                if overlap == None:
                    continue
                adding = (overlap[0] + (dest_start - source_start), overlap[1] + (dest_start - source_start))
                next_seeds.append(adding)
                ranges_added.append(overlap)
            # add missing ranges
            ranges_added = sorted(ranges_added, key=lambda x:x[0])
            ptr = seed[0]
            for r in ranges_added:
                if ptr < r[0]:
                    next_seeds.append((ptr, r[0]-1))
                    ptr = r[1]+1
                if ptr == r[0]:
                    ptr = r[1]+1
                if ptr > r[0]:
                    ptr = r[1]+1
            if ptr <= seed[1]:
                next_seeds.append((ptr, seed[1]))
        seeds = next_seeds
    
    if on_map and "map" not in line:
        k, start, rang = [*map(int, line.split(" "))]
        maps[-1][k] = (start, rang)

seed = min(seeds)[0]
for operation in maps[::-1]:
    for dest_start in operation:
        source_start, dist = operation[dest_start]
        if dest_start <= seed < dest_start + dist:
            seed = (seed - dest_start) + source_start
            break

part1 = min(seeds)
part2 = 0

print(f"part 1:")
print(f"{part1}")

print(f"part 2:")
print(f"{part2}")