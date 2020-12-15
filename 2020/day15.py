from toolbox import profile

inputs = [int(i) for i in open('inputs/day15.txt', 'r').read().strip().split(",")]

@profile
def run_alg(inputs, turns):
    counts = {v: [k+1] for k, v in enumerate(inputs)}
    last = inputs[-1]
    for turn in range(len(inputs), turns):
        s = 0
        if last in counts and len(counts[last]) > 1:
            s = counts[last][-1] - counts[last][-2]
        if s not in counts:
            counts[s] = []
        counts[s].append(turn + 1)
        if len(counts[s]) >= 3:
            counts[s].pop(0)
        last = s
    return s

part1 = run_alg(inputs, 2020)
print(f"part 1: {part1}")

part2 = run_alg(inputs, 30_000_000)
print(f"part 2: {part2}")