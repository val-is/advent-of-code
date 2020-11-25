data = open('inputs/day1.txt', 'r').read()

floors = []
for c in data:
    if c == "(":
        floors += [1]
    elif c == ")":
        floors += [-1]

print(f"part 1: {sum(floors)}")

s = 0
for pos, v in enumerate(floors):
    s += v
    if s < 0:
        break

print(f"part 2: {pos+1}")