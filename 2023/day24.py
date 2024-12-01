import sys
sys.setrecursionlimit(3000)

def step_stone(stone, p1=True):
    pos, vel = stone
    if p1:
        new_pos = (pos[0]+vel[0], pos[1]+vel[1], pos[2])
        return (new_pos, vel)
    return None

test_mi = 200000000000000
test_ma = 400000000000000
# test_mi = 7
# test_ma = 27
def test_in_area(stone):
    pos, _ = stone
    if not (test_mi <= pos[0] <= test_ma):
        return False
    if not (test_mi <= pos[1] <= test_ma):
        return False
    if not (test_mi <= pos[2] <= test_ma):
        return False
    return True

def ccw(A,B,C):
    return (C[1]-A[1]) * (B[0]-A[0]) > (B[1]-A[1]) * (C[0]-A[0])

def line_intersection(line1, line2):
    xdiff = (line1[0][0] - line1[1][0], line2[0][0] - line2[1][0])
    ydiff = (line1[0][1] - line1[1][1], line2[0][1] - line2[1][1])

    def det(a, b):
        return a[0] * b[1] - a[1] * b[0]

    div = det(xdiff, ydiff)
    if div == 0:
       return None

    d = (det(*line1), det(*line2))
    x = det(d, xdiff) / div
    y = det(d, ydiff) / div
    return x, y

# Return true if line segments AB and CD intersect
def intersect(A,B,C,D):
    return ccw(A,C,D) != ccw(B,C,D) and ccw(A,B,C) != ccw(A,B,D)

def in_past(stone, point):
    pos, vel = stone
    if pos[0] < point[0] and vel[0] < 0:
        return True
    if pos[1] < point[1] and vel[1] < 0:
        return True
    if pos[0] > point[0] and vel[0] > 0:
        return True
    if pos[1] > point[1] and vel[1] > 0:
        return True
    return False

def run(fname):
    lines = [line for line in open(fname, 'r').readlines()]

    part1 = 0
    part2 = 0

    stones = []

    for line in lines:
        a, b = line.strip().split(" @ ")
        x, y, z = map(int, a.split(", "))
        vx, vy, vz = map(int, b.split(", "))
        pos = (x, y, z)
        vel = (vx, vy, vz)

        stones.append((pos, vel))
    
    # stone_paths = {k: {v[0]} for k, v in enumerate(stones)}
    # stone_paths_ends = {k: [] for k, v in enumerate(stones)}
    stone_paths_ends = {}

    line_dist = 9999999999999999

    for k, stone in enumerate(stones):
        pos, vel = stone
        point_a = (pos[0]+vel[0]*-line_dist, pos[1]+vel[1]*-line_dist)
        point_b = (pos[0]+vel[0]*line_dist, pos[1]+vel[1]*line_dist)
        line = (point_a, point_b)
        a = line_intersection(line, ((test_mi, test_mi), (test_ma, test_mi)))
        b = line_intersection(line, ((test_mi, test_mi), (test_mi, test_ma)))
        c = line_intersection(line, ((test_ma, test_mi), (test_ma, test_ma)))
        d = line_intersection(line, ((test_mi, test_ma), (test_ma, test_ma)))
        ps = [v for v in [a, b, c, d] if v is not None]
        psps = []
        for p in ps:
            if not (test_mi <= p[0] <= test_ma):
                continue
            if not (test_mi <= p[1] <= test_ma):
                continue
            psps.append(p)
        # print(psps)
        # print(stone)
        if len(psps) != 2:
            continue
        # assert len(psps) == 2
        stone_paths_ends[k] = psps


    # stones_entered = {k: False for k, _ in enumerate(stones)}
    # stones_left = {k: False for k, _ in enumerate(stones)}
    # stones_considering = {k: True for k, _ in enumerate(stones)}

    # for k, stone in enumerate(stones):
    #     if test_in_area(stone):
    #         stones_entered[k] = True

    # done = False
    # i = 0
    # while not done:
    #     done = True
    #     i += 1
    #     for k, stone in enumerate(stones):
    #         if stones_left[k]:
    #             continue
    #         done = False

    #         updated = step_stone(stone)
    #         stones[k] = updated
    #         stone_paths[k] |= {updated[0]}
    #         in_area = test_in_area(updated)
            
    #         if stones_entered[k] and not in_area:
    #             stones_left[k] = True
    #             stone_paths_ends[k].append(stone[0])
    #         elif not stones_entered[k] and in_area:
    #             stone_paths_ends[k] = [stone[0]]
    #             stones_entered[k] = True
            
    
    for ka, _ in enumerate(stones):
        if ka not in stone_paths_ends:
            continue
        # print(stone_paths_ends[ka])
        for kb, _ in enumerate(stones):
            if kb not in stone_paths_ends:
                continue
            if ka == kb:
                continue
            # if len(stone_paths[ka] & stone_paths[kb]) > 0:
            #     part1 += 1
            # print(stone_paths_ends[ka], stone_paths_ends[kb])
            if intersect(stone_paths_ends[ka][0], stone_paths_ends[ka][1], stone_paths_ends[kb][0], stone_paths_ends[kb][1]):
                inttt = line_intersection(stone_paths_ends[ka], stone_paths_ends[kb])
                if in_past(stones[ka], inttt) or in_past(stones[kb], inttt):
                    continue
                part1 += 1
                # print(ka, kb)
    # print(stone_paths_ends)
            
    part1 /= 2

    import z3
    x, y, z = z3.Int("x"), z3.Int("y"), z3.Int("z")
    dx, dy, dz = z3.Int("dx"), z3.Int("dy"), z3.Int("dz")
    
    s = z3.Solver()
    for k, stone in enumerate(stones[:3]):
        pos, vel = stone
        t = z3.Int(f"{k}")
        s.add(z3.And(0 == x+dx*t - pos[0] - vel[0]*t))
        s.add(z3.And(0 == y+dy*t - pos[1] - vel[1]*t))
        s.add(z3.And(0 == z+dz*t - pos[2] - vel[2]*t))
    print(s.check())
    m = s.model()
    print(m[x]+m[y]+m[z])


    print(f"part 1:")
    print(f"{part1}")

    print(f"part 2:")
    print(f"{part2}")

# print("TEST")
# run('inputs/test.txt')
# print()
print("REAL")
run('inputs/day24.txt')