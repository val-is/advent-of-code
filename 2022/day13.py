inputs = open('inputs/day13.txt', 'r').read().split('\n\n')
ls = []
for i in inputs:
    a, b = [x.strip() for x in i.splitlines()]
    ls.append([eval(a), eval(b)])

def compare(a, b):
    if isinstance(a, list) and isinstance(b, list):
        idx = 0
        while True:
            if idx == len(a) and idx == len(b):
                return None
            if idx >= len(a):
                return True
            if idx >= len(b):
                return False
            v1, v2 = a[idx], b[idx]
            x = compare(v1, v2)
            idx += 1
            if x != None:
                return x
    elif isinstance(a, int) and isinstance(b, list):
        return compare([a], b)
    elif isinstance(a, list) and isinstance(b, int):
        return compare(a, [b])
    elif isinstance(a, int) and isinstance(b, int):
        if b < a:
            return False
        elif b == a:
            return None
        else:
            return True
    assert False

ok = []
for pair, v in enumerate(ls):
    if compare(v[0], v[1]):
        ok.append(pair+1)

part1 = sum(ok)
print(f"part 1: {part1}")


out = []
for a, b in ls:
    out.extend([a, b])
out.extend([[[2]], [[6]]])

import functools

def compare_sorting(a, b):
    # neg less, 0 eq, pos greater
    c = compare(a, b)
    if c == True:
        return -1
    elif c == False:
        return 99999999

out = sorted(out, key=functools.cmp_to_key(compare_sorting))
a = out.index([[2]])
b = out.index([[6]])
part2 = (a+1)*(b+1)

print(f"part 2: {part2}")