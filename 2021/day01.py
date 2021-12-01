inputs = [int(i) for i in open('inputs/day01.txt', 'r').readlines()]

part1 = 0
prev = inputs[0]
for i in inputs[1:]:
    if i > prev:
        part1 += 1
    prev = i

print(f"part 1: {part1}")

part2 = 0
window = inputs[0:3]
prev = sum(window)
for i in inputs[3:]:
    window += [i]
    if len(window) > 3:
        window = window[1:]
    s = sum(window)
    if s > prev:
        part2 += 1
    prev = s

print(f"part 2: {part2}")
