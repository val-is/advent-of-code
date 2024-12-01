import sys
# sys.setrecursionlimit(15000)

# def flood_fill(outline, start_coord):
#     frontier = [start_coord]
#     visited = set()
#     while len(frontier) > 0:
#         coord = frontier.pop(0)
#         for dx in [-1, 0, 1]:
#             for dy in [-1, 0, 1]:
#                 if dx == dy == 0:
#                     continue
#                 adj = (coord[0] + dx, coord[1] + dy)
#                 if adj in outline:
#                     continue
#                 if adj in visited:
#                     continue
#                 visited.add(adj)
#                 frontier.append(adj)
#     return visited

# OUTSIDE = 0
# ENTERING = 1
# LEAVING = 2
# IN_WALL = 3

# def line_parity_count(outline):
#     mi_x = ma_x = mi_y = ma_y = None
#     for i in outline:
#         if mi_x == None:
#             mi_x = i[0]
#             ma_x = i[0]
#             mi_y = i[1]
#             ma_y = i[1]
#         x, y = i
#         mi_x=  min(mi_x, x)
#         mi_y=  min(mi_y, y)
#         ma_x=  max(ma_x, x)
#         ma_y=  max(ma_y, y)
    
#     s = 0
#     for y in range(mi_y-1, ma_y+2):
#         state = OUTSIDE
#         acc = 0
#         for x in range(mi_x-1, ma_x+2):
#             if state == OUTSIDE:
#                 if (x, y) in outline:
#                     state = ENTERING
#                     acc = 1
#                 else:
#                     state = OUTSIDE
#             elif state == ENTERING:
#                 if (x, y) in outline:
#                     state = ENTERING
#                     acc += 1
#                 else:
#                     state = IN_WALL
#                     s += acc
#                     acc = 1
#             elif state == LEAVING:
#                 if (x, y) in outline:
#                     state = LEAVING
#                     acc += 1
#                 else:
#                     state = OUTSIDE
#                     s += acc
#             elif state == IN_WALL:
#                 if (x, y) in outline:
#                     state = LEAVING
#                     acc += 1
#                 else:
#                     state = IN_WALL
#                     acc += 1
#         if state == LEAVING or state == ENTERING:
#             s += acc
#     return s

fname = "inputs/day18.txt"
lines = [line for line in open(fname, 'r').readlines()]

def run(fname):
    
    coord = (0, 0)
    first_2 = []
    filled = {coord}

    part1 = 0
    coords = [coord]
    for line in lines:
        direction, distance, color = line.split(" ")

        distance = int(color[2:2+5], 16)
        direction = {
            "0": "R",
            "1": "D",
            "2": "L",
            "3": "U",
        }[color.strip()[-2]]

        distance = int(distance)
        if len(first_2) < 2:
            first_2.append(direction)
        dx, dy = {
            "U": (0, -1),
            "D": (0, 1),
            "R": (1, 0),
            "L": (-1, 0),
        }[direction]
        part1 += distance
        n_coord = (coord[0]+dx*distance, coord[1]+dy*distance)
        coords.append(n_coord)
        coord = n_coord
        # prev_coord = coord
        # for _ in range(int(distance)):
        #     coord = (coord[0]+dx, coord[1]+dy)
        #     filled.add(coord)
        # part1 += 0.5 * (prev_coord[1]+coord[1]) * (prev_coord[0]-coord[0])
        # print(coord)
    # inside = line_parity_count(filled) 
    for k, v in enumerate(coords[:-1]):
        part1 += (v[1] + coords[k+1][1]) * (v[0] - coords[k+1][0])
    part1 /= 2
    part1 += 1

    # part1 = inside
    part2 = 0

    # print(f"part 1:")
    # print(f"{part1}")

    # print(f"part 2:")
    # print(f"{part2}")

# print("TEST")
# run('inputs/test.txt')
# print()
# print("REAL")
import timeit
print(timeit.timeit(lambda: run('inputs/day18.txt'), number=10000)/10000)