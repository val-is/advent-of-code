def run(fname):
    lines = [i.strip() for i in open(fname, 'r').readlines()]

    for line in lines:
        string, verification = line.split(" ")
        verification = [*map(int, verification.split(","))]
    
    part1 = 0
    part2 = 0

    print(f"part 1:")
    print(f"{part1}")

    print(f"part 2:")
    print(f"{part2}")

print("TEST")
run('inputs/test.txt')
print()
print("REAL")
run('inputs/day12.txt')