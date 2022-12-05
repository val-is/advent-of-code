i = open("inputs/day05.txt", "r").read().split("\n\n")

crates = {}
for row in i[0].splitlines()[:-1]:
    chrs = [(k//4+1, v) for k, v in enumerate(row) if k % 4 == 1]
    for k, v in chrs:
        if v == " ":
            continue
        crates[k] = crates.get(k, []) + [v]

instrs = []
for instr in i[1].splitlines():
    _, a, _, b, _, c = instr.split()
    instrs.append((int(a), int(b), int(c)))


def output_crates(crates):
    return "".join([crates[i+1][0] for i in range(len(crates))])


# p1
cs_p1 = crates.copy()
for a, b, c in instrs:
    for _ in range(a):
        moving = cs_p1[b][0]
        cs_p1[b] = cs_p1[b][1:]
        cs_p1[c] = [moving] + cs_p1[c]
print(f"part 1: {output_crates(cs_p1)}")

# p2
cs_p2 = crates.copy()
for a, b, c in instrs:
    moving = cs_p2[b][:a]
    cs_p2[b] = cs_p2[b][a:]
    cs_p2[c] = moving + cs_p2[c]
print(f"part 2: {output_crates(cs_p2)}")
