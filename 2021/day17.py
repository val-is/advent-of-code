inputs = open('inputs/day17.txt', 'r').read().strip()

inputs = inputs[15:]
xbounds, ybounds = [[int(i) for i in j.split("..")] for j in inputs.split(", y=")]

def check_vel(vel_init):
    vel = vel_init
    pos = (0, 0)
    max_y = 0
    while pos[0] < xbounds[1] and pos[1] >= ybounds[0]:
        # print(pos, vel)
        pos = (pos[0]+vel[0], pos[1]+vel[1])
        max_y = max(max_y, pos[1])
        vx = 0
        if vel[0] >= 1:
            vx = vel[0]-1
        elif vel[0] <= -1:
            vx = vel[0]+1
        vel = (vx, vel[1]-1)
        if xbounds[0] <= pos[0] <= xbounds[1] and ybounds[0] <= pos[1] <= ybounds[1]:
            return True, max_y
    return False, 0

possible_vels = set()
part1 = 0
for x in range(0, 1000):
    for y in range(-1000, 1000):
        valid, max_y = check_vel((x, y))
        if valid:
            possible_vels.add((x, y))
            part1 = max(part1, max_y)
print(f"part 1: {part1}")

part2 = len(possible_vels)
print(f"part 2: {part2}")
