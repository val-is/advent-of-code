dat = open("inputs/day03.txt", "r").read()

part1 = 0
part2 = 0

dat = dat.replace("mul(", "=")
dat = dat.replace("do()", "\\")
dat = dat.replace("don't()", "|")

enabled = True
read_state = 0  # 1 2 3
n1 = ""
n2 = ""
for i in dat:
    if i == "\\":
        enabled = True
    if i == "|":
        enabled = False

    if read_state == 0:
        if i == "=":
            read_state = 1
            n1 = ""
            n2 = ""
    elif read_state == 1:
        if i in "0123456789":
            n1 += i
        elif i == ",":
            read_state = 2
        else:
            read_state = 0
    elif read_state == 2:
        if i in "0123456789":
            n2 += i
            read_state = 3
        else:
            read_state = 0
    elif read_state == 3:
        if i in "0123456789":
            n2 += i
        elif i == ")":
            # done!
            if enabled:
                part2 += int(n1) * int(n2)
            part1 += int(n1) * int(n2)

            read_state = 0
        else:
            # invalid
            read_state = 0


print(f"part 1:")
print(f"{part1}")

print(f"part 2:")
print(f"{part2}")
