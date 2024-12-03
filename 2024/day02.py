lines = [i for i in open("input.txt", "r").readlines()]

part1 = 0
part2 = 0

for line in lines:
    ns_real = [*map(int, line.split(" "))]
    any_safe = False
    for skip in range(len(ns_real)):
        ns = ns_real[:skip] + ns_real[skip + 1 :]
        safe = True
        prev = ns[0]
        direction = None
        for i in ns[1:]:
            if direction == None:
                if i > prev:
                    direction = 1
                elif i < prev:
                    direction = -1
                else:
                    direction = 0
            else:
                if i > prev and direction != 1:
                    safe = False
                elif i < prev and direction != -1:
                    safe = False
            prev = i
        prev = ns[0]
        for i in ns[1:]:
            dist = abs(i - prev)
            if dist < 1 or dist > 3:
                safe = False
            prev = i
        if safe:
            any_safe = True
    if any_safe:
        part1 += 1

print(f"part 1:")
print(f"{part1}")

print(f"part 2:")
print(f"{part2}")
