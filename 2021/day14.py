from collections import Counter

inputs = open('inputs/day14.txt', 'r').read()

code, raw_rules = inputs.strip().split("\n\n")

rules = {}

for i in raw_rules.split("\n"):
    a, b = i.strip().split(" -> ")
    rules[a] = b

def step(pairs, rules):
    n_pairs = Counter()
    for k in pairs:
        n = pairs[k]
        if k in rules:
            n_pairs[k[0] + rules[k]] += n
            n_pairs[rules[k] + k[1]] += n
        else:
            n_pairs[k] += n
    return n_pairs

def calc_quans(counts):
    cs = Counter()
    for c in counts:
        for i in c:
            cs[i] += counts[c]
    com = cs.most_common()
    return com[0][1]//2 - com[-1][1]//2

def gen_pairs(s):
    pairs = Counter()
    for i in range(len(s)-1):
        pairs[s[i:i+2]] += 1
    return pairs

def r(code, iters):
    cs = gen_pairs(code)
    for _ in range(iters):
        cs = step(cs, rules)
    return calc_quans(cs)

part1 = r(code, 10)
print(f"part 1: {part1}")

part2 = r(code, 40)
print(f"part 2: {part2}")
