inputs = [i.strip() for i in open('inputs/day11.txt').read().split("\n\n")]

monkeys = []
div_bys = set()

for idx, case in enumerate(inputs):
    lines = [i.strip() for i in case.splitlines()]
    starting_items = [int(i) for i in lines[1].split(': ', 1)[1].split(', ')]
    operation = lines[2].split(": ", 1)[1].split(' ')[3:]
    test = int(lines[3].split("by ", 1)[1])
    div_bys.add(test)
    if_true = int(lines[4].split('monkey ', 1)[1])
    if_false = int(lines[5].split('monkey ', 1)[1])

    monkeys.append([
        starting_items, operation, test, if_true, if_false
    ])

gcf = 1
for a in div_bys:
    gcf *= a


def eval_monkey(idx, instructions, inventory, part1=True):
    # returns map [idx] -> where each item goes
    output = {}
    _, operation, test, if_true, if_false = instructions
    for item in inventory:
        worry_level = item
        acc = operation[1]
        if acc == 'old':
            acc = worry_level
        else:
            acc = int(acc)
        if operation[0] == '*':
            worry_level *= acc
        elif operation[0] == '+':
            worry_level += acc

        if part1:
            worry_level = worry_level // 3
        else:
            worry_level = worry_level % gcf
        if worry_level % test == 0:
            output[if_true] = output.get(if_true, []) + [worry_level]
        else:
            output[if_false] = output.get(if_false, []) + [worry_level]
    return output


def run_iters(times, part1=True):
    monkey_invs = {}
    for idx, monkey in enumerate(monkeys):
        monkey_invs[idx] = [*monkey[0]]

    inspection_counts = {}

    # do instr
    for _ in range(times):
        for idx, monkey_instr in enumerate(monkeys):
            inspection_counts[idx] = inspection_counts.get(
                idx, 0) + len(monkey_invs[idx])
            output = eval_monkey(
                idx, monkey_instr, monkey_invs[idx], part1=part1)
            monkey_invs[idx] = []
            for i in output:
                monkey_invs[i].extend(output[i])

    vs = [inspection_counts[i] for i in inspection_counts]
    a, b = sorted(vs)[::-1][:2]
    return a*b


part1 = run_iters(20)
print(f"part 1: {part1}")

part2 = run_iters(10_000, part1=False)
print(f"part 2: {part2}")
