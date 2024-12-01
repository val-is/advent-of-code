def find_symm(bms):
    possible = []
    for split in range(1, len(bms)):
        a, b = bms[:split], bms[split:]
        a = a[::-1]
        sym = True
        for k in range(min(len(a), len(b))):
            if a[k] != b[k]:
                sym = False
                break
        if sym:
            possible.append(split)
    return possible

# def find_diff_1b(bms):
#     possible = []
#     for a in range(1, len(bms)):
#         if (bms[a]^bms[a-1]).bit_count() == 1:
#             possible.append(a)
#     return possible

import math
def brutus(bms):
    possible = []
    max_int = max(bms)
    max_int=int(math.log2(max_int))+3
    for y in range(len(bms)):
        for x in range(max_int+1):
            bms[y] ^= 1<<x

            rs= find_symm(bms)
            if len(rs) != 0:
                possible.extend(rs)

            bms[y] ^= 1<<x
    return possible
        

def render(bms, max_x, max_y):
    for y in range(max_y+1):
        for x in range(max_x+1):
            if bms[y]&(1<<x):
                print("#", end="")
            else:
                print(".", end="")
        print()
    print()

def run(fname):
    squares = open(fname, 'r').read().split("\n\n")
    part1 = 0
    part2 = 0
    for square in squares:
        square = square.strip().split("\n")
        mapping = {}
        max_y = 0
        max_x = 0
        for y, row in enumerate(square):
            max_y = y
            for x, val in enumerate(row):
                mapping[x, y] = val
                max_x = x
        row_bitmasks = []
        cols_bitmasks = []
        for y in range(max_y+1):
            bm = 0
            for x in range(max_x+1):
                bm |= (1 if mapping[x, y] == "#" else 0)<<x
            row_bitmasks.append(bm)
        for x in range(max_x+1):
            bm = 0
            for y in range(max_y+1):
                bm |= (1 if mapping[x, y] == "#" else 0)<<y
            cols_bitmasks.append(bm)
        
        rs= find_symm(row_bitmasks)
        cs= find_symm(cols_bitmasks)
        if len(rs) != 0:
            part1 += rs[0]*100
        elif len(cs) != 0:
            part1 += cs[0]
        else:
            assert False
        a = set(brutus(row_bitmasks))
        a -= set(rs)
        if len(a) != 0:
            part2 += a.pop()*100
            continue
        a = set(brutus(cols_bitmasks))
        a -= set(cs)
        if len(a) != 0:
            part2 += a.pop()
            continue
        assert False
        

    print(f"part 1:")
    print(f"{part1}")

    print(f"part 2:")
    print(f"{part2}")

print("TEST")
run('inputs/test.txt')
print()
print("REAL")
run('inputs/day13.txt')