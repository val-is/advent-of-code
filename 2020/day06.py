inputs = [i.strip() for i in open('inputs/day6.txt', 'r').read().split('\n\n')]

part1 = 0
for i in inputs:
    c = set()
    for k in i.replace("\n", ""):
        c.add(k)
    part1 += len(c)

print(f"part 1: {part1}")

part2 = 0
for i in inputs:
    c = set()
    for k, v in enumerate(i.split("\n")):
        s = set()
        for char in v:
            s.add(char)
            
        if k != 0:
            c = c.intersection(s)
        else:
            c = s
    part2 += len(c)
print(f"part 2: {part2}")