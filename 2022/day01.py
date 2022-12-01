lines = [i for i in open('inputs/day01.txt', 'r').readlines()]

calories = []

group = []
for line in lines:
    line = line.strip()
    if line == "":
        calories.append(sum(group))
        group = []
    else:
        group.append(int(line))
calories.append(sum(group))
print(f"part 1: {max(calories)}")

calories = sorted(calories)[::-1]
print(f"part 2: {sum(calories[0:3])}")