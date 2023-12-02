lines = [i for i in open('inputs/day01.txt', 'r').readlines()]

part1 = 0
part2 = 0

for line in lines:
    f = ""
    l = ""
    for i in line:
        if i in "1234567890":
            if f == "":
                f = i
            l=i
    part1 += int(f+l)

m = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
    "zero": 0,
}

for line in lines:
    l = line
    f = ""
    last = ""
    for x in range(len(l)):
        try:
            for lllll in range(6):
                if l[x:x+lllll] in m:
                    if f == "":
                        f = m[l[x:x+lllll]]
                    last = m[l[x:x+lllll]]
            if l[x] in "1234567890":
                if f == "":
                    f = l[x]
                last = l[x]
        except:
            pass
    part2 += int(str(f)+str(last))

print(f"part 1:")
print(f"{part1}")

print(f"part 2:")
print(f"{part2}")