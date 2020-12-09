inputs = [int(i) for i in open('inputs/day9.txt', 'r').readlines()]
preamb = 25

def check_validity(index):
    prev = inputs[index-preamb:index]
    for i in prev:
        for j in prev:
            if i + j == inputs[index] and i != j:
                return True
    return False

part1 = 0
for i in range(preamb, len(inputs)):
    if not check_validity(i):
        part1 = inputs[i]
        break
print(f"Part 1: {part1}")

def check_sums(start):
    acc = 0
    mi = max(inputs)
    ma = 0
    for i in range(start, len(inputs)):
        mi = min(inputs[i], mi)
        ma = max(inputs[i], ma)
        acc += inputs[i]
        if acc == part1:
            return mi + ma
    return -1

part2 = 0
for i in range(len(inputs)):
    if (j := check_sums(i)) != -1:
        part2 = j
        break
print(f"Part 2: {part2}")