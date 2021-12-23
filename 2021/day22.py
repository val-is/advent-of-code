inputs = open('inputs/day22.txt', 'r').readlines()

steps = []

for i in inputs:
    toggle, dims = i.strip().split(" ")
    dims = dims.split(",")
    def parse_dim(dim):
        a,b =  [int(i) for i in dim[2:].split("..")]
        return (a, b)
    x, y, z = [parse_dim(d) for d in dims]
    steps.append((toggle, (x, y, z)))

# grid = {}

# for k, s in enumerate(steps):
#     mode = True if s[0] == "on" else False
#     for x in range(s[1][0][0], s[1][0][1]+1):
#         if not (-50 <= x <= 50):
#             continue
#         for y in range(s[1][1][0], s[1][1][1]+1):
#             if not (-50 <= y <= 50):
#                 continue
#             for z in range(s[1][2][0], s[1][2][1]+1):
#                 if not (-50 <= z <= 50):
#                     continue
#                 grid[x,y,z] = mode
# s = 0
# for i in grid:
#     x, y, z = i
#     if grid[i]:
#         s += 1

# part1 = s
# print(f"part 1: {part1}")

# class vec3:
#     def __init__(self, x, y, z):
#         self.x = x
#         self.y = y
#         self.z = z

# def get_cube_intersection(a1, a2, b1, b2):
#     if a1.x > b2.x:
#         return
#     if a1.x > b2.x:
#         return
#     if a2.x < b1.x:
#         return
#     if a1.y > b2.y:
#         return
#     if a2.y < b1.y:
#         return
#     if a1.z > b2.z:
#         return
#     if a2.z < b1.z:
#         return
#     xs = sorted([a1.x, a2.x, b1.x, b2.x])[1:3]
#     ys = sorted([a1.y, a2.y, b1.y, b2.y])[1:3]
#     zs = sorted([a1.z, a2.z, b1.z, b2.z])[1:3]
#     return vec3(xs[0], ys[0], zs[0]), vec3(xs[1], ys[1], zs[1])

# def get_cube_decomposition(a2, a2, b1, b2):
#     xs = set(sorted([a1.x, a2.x, b1.x, b2.x]))
#     ys = set(sorted([a1.y, a2.y, b1.y, b2.y]))
#     zs = set(sorted([a1.z, a2.z, b1.z, b2.z]))

# def get_vol(a, b):
#     return abs(a.x-b.x) * abs(a.y-b.y) * abs(a.z-b.z)

# patches = []

# for instruction in steps:
#     mode = True if s[0] == "on" else False
#     corner_a = vec3(s[1][0][0], s[1][1][0], s[1][2][0])
#     corner_b = vec3(s[1][0][1], s[1][1][1], s[1][2][1])
    
#     if mode:
#         for patch in patches:
#             i = get_cube_intersection(corner_a, corner_b, a[0], a[1])
#             if i == None:
#                 continue

def clamp_range(a, b, mi, ma):
    if b < mi:
        return []
    if a > ma:
        return []
    return range(max(mi, a), min(ma, b)+1)

def count(state, a, b, prev):
    vol = abs(a[0]-b[0]-1) * abs(a[1]-b[1]-1) * abs(a[2]-b[2]-1)
    overlapping_areas = []
    for past in prev:
        mode_o, zz = past
        a_o, b_o = (zz[0][0], zz[1][0], zz[2][0]), (zz[0][1], zz[1][1], zz[2][1])
        xs, ys, zs = [clamp_range(a_o[i], b_o[i], a[i], b[i]) for i in range(3)]
        if len(xs) == 0 or len(ys) == 0 or len(zs) == 0:
            continue
        overlapping_areas.append([mode_o, [[xs[0], xs[-1]], [ys[0], ys[-1]], [zs[0], zs[-1]]]])
    for k, v in enumerate(overlapping_areas):
        vol -= count(v[0], (v[1][0][0], v[1][1][0], v[1][2][0]), (v[1][0][1], v[1][1][1], v[1][2][1]), overlapping_areas[k+1:])
    return vol

su = 0
for k, s in enumerate(steps):
    mode = True if s[0] == "on" else False
    if not mode:
        continue
    c = count(mode, 
            (s[1][0][0], s[1][1][0], s[1][2][0]),
            (s[1][0][1], s[1][1][1], s[1][2][1]), steps[k+1:])
    su += c

part2 = su
print(f"part 2: {part2}")
