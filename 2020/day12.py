from toolbox import memoize_the_world, profile

inputs = [i.strip() for i in open('inputs/day12.txt', 'r').readlines()]

EAST, NORTH, WEST, SOUTH = range(4)

def manhattan_dist(pos):
    return sum([abs(i) for i in pos])

# @profile
def run_commands(commands, process_func, state):
    for command in commands:
        state = process_func(
            (command[0], int(command[1:])),
            state)
    return manhattan_dist(state[0]) # state is always (pos, ...)

@memoize_the_world
def process_command_p1(instr, state):
    pos, facing = state
    command, amount = instr
    x, y = pos
    if command in "NSEW":
        x += {"E": 1, "W": -1}.get(command, 0) * amount
        y += {"N": 1, "S": -1}.get(command, 0) * amount
    elif command in "RL":
        facing += (amount // 90) * {"L": 1, "R": -1}[command]
        facing %= 4
    elif command in "F":
        x += {EAST: 1, WEST: -1}.get(facing, 0) * amount
        y += {NORTH: 1, SOUTH: -1}.get(facing, 0) * amount
    return (x, y), facing

part1 = run_commands(inputs, process_command_p1,
                    ((0, 0), EAST))
print(f"part 1: {part1}")

@memoize_the_world
def process_command_p2(instr, state):
    pos, facing, waypoint = state
    command, amount = instr
    sX, sY = pos
    wX, wY = waypoint
    if command in "NSEW":
        wX += {"E": 1, "W": -1}.get(command, 0) * amount
        wY += {"N": 1, "S": -1}.get(command, 0) * amount
    elif command in "RL":
        a = 1 if command == "R" else -1
        for _ in range(amount // 90):
            wX, wY = a*wY, a*-wX
    elif command in "F":
        sX += wX * amount
        sY += wY * amount
    return (sX, sY), facing, (wX, wY)

part2 = run_commands(inputs, process_command_p2,
                    ((0, 0), EAST, (10, 1)))
print(f"part 2: {part2}")