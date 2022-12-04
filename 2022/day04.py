inputs = [i.strip() for i in open("inputs/day04.txt", 'r').readlines()]

score = 0
for i in inputs:
    a, b = i.split(",")
    a1, a2 = [int(j) for j in a.split("-")]
    b1, b2 = [int(j) for j in b.split("-")]

    if a1 <= b1 <= a2 and a1 <= b2 <= a2:
        score += 1
        continue
    if b1 <= a1 <= b2 and b1 <= a2 <= b2:
        score += 1
        continue

print(f"part 1: {score}")

score = 0
for i in inputs:
    a, b = i.split(",")
    a1, a2 = [int(j) for j in a.split("-")]
    b1, b2 = [int(j) for j in b.split("-")]

    if a1 <= b1 <= a2 or a1 <= b2 <= a2:
        score += 1
        continue
    if b1 <= a1 <= b2 or b1 <= a2 <= b2:
        score += 1
        continue
print(f"part 2: {score}")
