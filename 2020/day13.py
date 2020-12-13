from toolbox import profile

inputs = [i.strip() for i in open('inputs/day13.txt', 'r').readlines()]

earliest = int(inputs[0])
busses = []
for k, v in enumerate(inputs[1].split(",")):
    if v != "x":
        busses += [(k, int(v))]

# @profile
def solve_p1(bIn):
    busses = bIn.copy()
    t = earliest
    while True:
        for b in busses:
            if b == None:
                continue
            if (t % b[1]) == 0:
                return (t - earliest) * b[1]
        t += 1

part1 = solve_p1(busses)
print(f"part 1: {part1}")

# @profile
def solve_p2(bIn):
    busses = bIn.copy()
    min_matched = 1
    t = earliest
    while True:
        index, bus = busses[0]
        if (t+index) % bus == 0:
            min_matched *= bus
            busses.pop(0)
        if len(busses) == 0:
            return t
        t += min_matched

part2 = solve_p2(busses)
print(f"part 2: {part2}")