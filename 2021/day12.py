inputs = open('inputs/day12.txt', 'r').readlines()

caves = {}

n = set()

for line in inputs:
    start, end = line.strip().split("-")
    if start not in caves:
        caves[start] = set()
    caves[start].add(end)
    if end not in caves:
        caves[end] = set()
    caves[end].add(start)
    n.add(start)
    n.add(end)

for i in n:
    if i not in caves:
        caves[i] = set()

def p1_traverse(caves, current, traversed_small, past):
    past += "-" + current
    # print(past, traversed_small, caves[current])
    if current == "start" and past != "-start":
        return 0
    if current == "end":
        return 1
    possible = 0
    for adj in caves[current]:
        if adj == adj.lower():
            if adj in traversed_small:
                continue
            else:
                new_trav = {i for i in traversed_small}
                new_trav.add(adj)
                possible += p1_traverse(caves, adj, new_trav, past)
        else:
            new_trav = {i for i in traversed_small}
            possible += p1_traverse(caves, adj, new_trav, past)
    return possible

part1 = p1_traverse(caves, "start", set(), "")
print(f"part 1: {part1}")

def copydict(d):
    new_d = {k: d[k] for k in d}
    return new_d

def twice_used(d):
    for k in d:
        if d[k] >= 2:
            return True
    return False

def p2_traverse(caves, current, traversed_small, past):
    past += "-" + current
    if current == "start" and past != "-start":
        return 0
    if current == "end":
        return 1
    possible = 0
    for adj in caves[current]:
        if adj == adj.lower():
            if adj in traversed_small and twice_used(traversed_small):
                continue
            else:
                new_trav = copydict(traversed_small)
                if adj in new_trav:
                    new_trav[adj] += 1
                else:
                    new_trav[adj] = 1
                possible += p2_traverse(caves, adj, new_trav, past)
        else:
            new_trav = copydict(traversed_small)
            possible += p2_traverse(caves, adj, new_trav, past)
    return possible

part2 = p2_traverse(caves, "start", {}, "")
print(f"part 2: {part2}")
