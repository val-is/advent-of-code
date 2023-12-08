lines = [i.strip() for i in open('inputs/day06.txt', 'r').readlines()]

# race_stats = [
#     [7, 9],
#     [15, 40],
#     [30, 200]
# ]
# race_stats = [
#     [57, 291],
#     [72, 1172],
#     [69, 1176],
#     [92, 2026]
# ]

# race_stats = [
#     [71530, 940200]
# ]
race_stats = [
    [57726992, 291117211762026]
]

p = 1
for race in race_stats:
    time, distance = race
    i = 0
    valid = 0
    while True:
        trav = i * (time - i)
        if trav > distance:
            valid += 1
        i += 1
        if i > time:
            break
    p *= valid

part1 = p
part2 = 0

print(f"part 1:")
print(f"{part1}")

print(f"part 2:")
print(f"{part2}")