lines = [i.strip() for i in open('inputs/day08.txt', 'r').readlines()]

directions = lines[0].strip()
lines = lines[2:]

tree = {}
for i in lines:
    key, vals = i.strip().split(" = ")
    vals = vals.replace("(", "")
    vals = vals.replace(")", "")
    vals = vals.split(", ")
    tree[key] = (vals[0], vals[1])

nodes = [node for node in tree if node[2] == "A"]
occur = [-1 for _ in nodes]
part1 = 0
cur = "AAA"
ptr = 0
while True:
    direction = directions[ptr]
    ptr += 1
    if ptr >= len(directions):
        ptr = 0
    all_clear = True
    for k, node in enumerate(nodes):
        if node[2] == "Z" and occur[k] == -1:
            occur[k] = part1
    if -1 not in occur:
        break
    for node in nodes:
        if node[2] != "Z":
            all_clear = False
            break
    if all_clear:
        break
    part1 += 1
    next_nodes = []
    if direction == "R":
        for node in nodes:
            next_nodes.append(tree[node][1])
    else:
        for node in nodes:
            next_nodes.append(tree[node][0])
    nodes = next_nodes
part2 = 1
import math
def lcm(a, b):
    return abs(a*b) // math.gcd(a, b)
for i in occur:
    part2 = lcm(part2, i)

print(f"part 1:")
print(f"{part1}")

print(f"part 2:")
print(f"{part2}")