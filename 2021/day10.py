inputs = open('inputs/day10.txt', 'r').readlines()

pairs = {
    "[":"]",
    "(":")",
    "{":"}",
    "<":">"
}

def build_stack(i):
    stack = []
    for k in i:
        if k in pairs:
            stack.append(k)
        else:
            if pairs[stack[-1]] != k:
                return k, True
            else:
                stack.pop(len(stack)-1)
    return stack, False

part1 = 0

def score_char(char):
    return {
        ")": 3,
        "]": 57,
        "}": 1197,
        ">": 25137,
    }[char]

for idx, i in enumerate(inputs):
    char, corrupted = build_stack(i.strip())
    if corrupted:
        part1 += score_char(char)

print(f"part 1: {part1}")

def get_endstop(i):
    i = i[::-1]
    s = ""
    for j in i:
        s += pairs[j]
    return s

def score_endstop(endstop):
    s = 0
    for i in endstop:
        s *= 5
        s += {")":1,"]":2,"}":3,">":4}[i]
    return s

part2 = []
for i in inputs:
    stack, corrupted = build_stack(i.strip())
    if not corrupted:
        x = get_endstop(stack)
        part2.append(score_endstop(x))

part2 = sorted(part2)[int(len(part2)/2)]
print(f"part 2: {part2}")
