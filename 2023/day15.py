def hash_str(string):
    acc = 0
    for s in string:
        acc += ord(s)
        acc *= 17
        acc %= 256
    return acc

def run(fname):
    lines = [f for f in open(fname, 'r').read().strip().split(",")]

    part1 = 0
    for l in lines:
        part1 += hash_str(l)
    
    hh = {}
    for l in lines:
        if "-" in l:
            ss = l[:-1]
            box = hash_str(ss)
            if box not in hh:
                continue
            else:
                for ls in hh[box]:
                    rms = []
                    if ls[0] == ss:
                        rms.append(ls)
                    for ls in rms:
                        hh[box].remove(ls)
        elif "=" in l:
            ss, val = l.split("=")
            val = int(val)
            box = hash_str(ss)
            if box not in hh:
                hh[box] = [[ss, val]]
            else:
                present = False
                for k, ls in enumerate(hh[box]):
                    if ls[0] == ss:
                        ls[1] = val
                        present = True
                if not present:
                    hh[box].append([ss, val])

    part2 = 0
    for i in range(256):
        if i in hh:
            for k, v in enumerate(hh[i]):
                part2 += (i+1)*(k+1)*v[1]

    print(f"part 1:")
    print(f"{part1}")

    print(f"part 2:")
    print(f"{part2}")

print("TEST")
run('inputs/test.txt')
print()
print("REAL")
run('inputs/day15.txt')