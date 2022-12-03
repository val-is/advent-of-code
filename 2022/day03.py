inputs = [i.strip() for i in open("inputs/day03.txt", 'r').readlines()]

priorities = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

def get_prio(c):
    return priorities.index(c)

score = 0
for sack in inputs:
    a, b = sack[:len(sack)//2], sack[len(sack)//2:]
    s1 = set([i for i in a])
    s2 = set([i for i in b])
    u = s1 & s2
    item = u.pop()
    score += get_prio(item)

print(f"part 1: {score}")

g = []
groups = []
for i in inputs:
    if len(g) == 3:
        a, b, c = [set(i) for i in g]
        u = a & b & c
        groups.append(u.pop())
        n = 0
        g = []
    g.append(i)
a, b, c = [set(i) for i in g]
u = a & b & c
groups.append(u.pop())

score = 0
for g in groups:
    score += get_prio(g)
print(f"part 2: {score}")
