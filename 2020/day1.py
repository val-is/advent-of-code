inputs = [int(i) for i in open('inputs/day1.txt', 'r').readlines()]

part1 = 0
for i in inputs:
    for j in inputs:
        if i != j and i + j == 2020:
            part1 = i*j
            break
print(f"part 1: {part1}")

part2 = 0
for i in inputs:
    for j in inputs:
        for k in inputs:
            if i != j != k and i + j + k == 2020:
                part2 = i*j*k
                break
print(f"part 2: {part2}")