lines = [i for i in open("inputs/day01.txt", "r").readlines()]

part1 = 0
part2 = 0


aa = []
bb = []

for line in lines:
    a, b = map(int, line.split())
    aa.append(a)
    bb.append(b)
aa = sorted(aa)
bb = sorted(bb)

for i in range(len(aa)):
    part1 += abs(aa[i] - bb[i])

part1 += 0

for i in range(len(aa)):
    times = len([j for j in bb if j == aa[i]])
    part2 += aa[i] * times


print(f"part 1:")
print(f"{part1}")

print(f"part 2:")
print(f"{part2}")
