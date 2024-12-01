import sys
# sys.setrecursionlimit(15000)

def get_inf(mm, pos, max_x, max_y):
    p_x = pos[0]%(max_x+1)
    p_y = pos[1]%(max_y+1)
    return mm[p_x, p_y]

def run(fname):
    lines = [line for line in open(fname, 'r').readlines()]

    mm = {}
    start_pos = ()
    max_x = 0
    max_y = 0
    for y, row in enumerate(lines):
        for x, val in enumerate(row.strip()):
            mm[x, y] = val
            if val == "S":
                start_pos = (x, y)
            max_x = max(x, max_x)
        max_y = max(y, max_y)

    current = {start_pos}
    adj_plots = set()
    s = 0
    while True:
        s += 1
        next_visiting = set()
        adj_plots = set()
        for pos in current:
            for dx, dy in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                p = (pos[0]+dx, pos[1]+dy)
                ppp = get_inf(mm, p, max_x, max_y)
                if ppp == "." or ppp == "S":
                    next_visiting.add(p)
                    adj_plots.add(p)
        current = next_visiting
        
        target = (max_x/2)+max_x*2
        target = 26501365 % max_x
        if s == 4*(max_x+1)+target:
            print(s, len(adj_plots))
        if s == 10_000:
            break
        # if len(adj_plots) == 26501365:
        #     break

    part1 = len(adj_plots)
    part2 = s
    
    print(f"part 1:")
    print(f"{part1}")

    print(f"part 2:")
    print(f"{part2}")

# print("TEST")
# run('inputs/test.txt')
print()
print("REAL")
run('inputs/day21.txt')