inputs = [i.strip() for i in open('inputs/day10.txt', 'r').readlines()]

X = 1
vals = []

def is_drawing(cycle, X):
    cycle = cycle % 40
    if cycle == 0: cycle = 40
    if X<= (cycle) <= X+2:
        return True
    return False
cycle = 0
s = ""
for instr in inputs:
    if instr.startswith('noop'):
        cycle += 1
        s += "#" if is_drawing(cycle, X) else "."
        vals.append(X)
    else:
        a, b = instr.split()
        cycle += 1
        s += "#" if is_drawing(cycle, X) else "."
        vals.append(X)
        cycle += 1
        s += "#" if is_drawing(cycle, X) else "."
        vals.append(X)
        X += int(b)

ss = ""
for idx, v in enumerate(s):
    if idx % 40 == 0:
        ss+="\n"
    ss+=v

interesting = []
i = 20-1
while i < len(vals):
    interesting.append(vals[i] * (i+1))
    i += 40

part1 = sum(interesting)
print(f"part 1: {part1}")

print("part 2:")
print(ss)