from toolbox import memoize, profile
import re

inputs = [i.strip() for i in open("inputs/day14.txt", 'r').readlines()]

def apply_mask(mask, v):
    # mask = 11X01X101X10000110110101X100000011XX
    acc = 0
    for k, maskV in enumerate(mask[::-1]):
        if maskV == "X":
            acc += v & (2**k)
        else:
            acc += (2**k) * int(maskV)
    return acc

curMask = 0
acc = {}
part1 = 0

for i in inputs:
    if i.startswith("mask = "):
        curMask = i[7:]
    else:
        mem = int(re.match(r"^mem\[([0-9]+)\].*$", i)[1])
        acc[mem] = apply_mask(curMask, int(i.split("= ")[1]))

part1 = sum(acc.values())
print(f"part 1: {part1}")


# switching to strings. that was hell

def replace_in_str(s, pos, v):
    return s[:pos] + v + s[pos+1:]

@memoize
def get_floating(mem):
    for k, v in enumerate(mem):
        if v == "X":
            a = b = mem
            a = replace_in_str(a, k, "0")
            b = replace_in_str(b, k, "1")
            return get_floating(a) + get_floating(b)
    return [mem]

tape = {}
curMask = 0
for i in inputs:
    if i.startswith("mask"):
        curMask = i[7:]
    else:
        matches = re.match(r"^mem\[([0-9]+)\] = ([0-9]+)$", i)
        mem, value = f"{int(matches[1]):036b}", int(matches[2])
        for k, v in enumerate(curMask):
            if v != "0":
                mem = replace_in_str(mem, k, v)
        for addr in get_floating(mem):
            tape[int(addr, 2)] = value

part2 = sum(tape.values())
print(f"part 2: {part2}")
