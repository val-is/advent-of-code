def iteration(ll):
    out = []
    prev = ll[0]
    if len(ll) == 1:
        return [prev]
    for x in ll[1:]:
        out.append(x-prev)
        prev = x
    return out

def all_zero(ll):
    for i in ll:
        if i != 0: return False
    return True

def extrapolate(histories):
    next_adding = None
    for k in range(len(histories))[::-1]:
        if next_adding == None:
            histories[k].append(0)
        else:
            histories[k].append(histories[k][-1]+next_adding)
        next_adding = histories[k][-1]

def run(fname):
    lines = [i.strip() for i in open(fname, 'r').readlines()]
    ll = [[*map(int, line.split(" "))] for line in lines]

    part1 = 0

    for line in ll:
        histories = [line]
        while True:
            if all_zero(histories[-1]):
                break
            histories.append(iteration(histories[-1]))
        extrapolate(histories)
        part1 += histories[0][-1]

    part2 = 0

    for line in ll:
        histories = [line[::-1]]
        while True:
            if all_zero(histories[-1]):
                break
            histories.append(iteration(histories[-1]))
        extrapolate(histories)
        part2 += histories[0][-1]

    print(f"part 1:")
    print(f"{part1}")

    print(f"part 2:")
    print(f"{part2}")

# print("TEST")
# run('inputs/test.txt')
print()
print("REAL")
run('inputs/day09.txt')
