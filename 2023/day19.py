import sys
# sys.setrecursionlimit(15000)

def eval_workflow(part, workflow):
    for rule in workflow[0]:
        if rule[0](part):
            # print(rule, part, part[rule[2][0]], rule[2][1])
            return rule[1]
    return workflow[1]

def get_overlapping_range(a1, a2, b1, b2):
    lhs = max(a1, b1)
    rhs = min(a2, b2)
    if lhs > rhs:
        return None
    return lhs, rhs

def get_range_size(a1, a2):
    return a2-a1+1

def get_non_overlapping_ranges(a1, a2, b1, b2):
    rs = []
    if a2 < b1:
        rs.append((a1, a2))
    if a1 < b1 < a2:
        rs.append((a1, b1-1))
    if a1 < b2 < a2:
        rs.append((b2+1, a2))
    if b2 < a1:
        rs.append((a1, a2))
    return rs

PART_MAX = 4000
def split_workflow_rule(ranged_part, rule):
    accepted = [] # (part {x:range, y:range,....}, next)
    rejected = []
    opz, operation = rule[2], rule[3]
    if operation == ">":
        accepted_parts = get_overlapping_range(ranged_part[opz[0]][0], ranged_part[opz[0]][1], int(opz[1])+1, PART_MAX)
        if accepted_parts != None:
            ss = {k: ranged_part[k] for k in ranged_part}
            ss[opz[0]] = accepted_parts
            accepted.append((ss, rule[1]))
        rejected_parts = get_non_overlapping_ranges(ranged_part[opz[0]][0], ranged_part[opz[0]][1], int(opz[1])+1, PART_MAX)
        for r in rejected_parts:
            ss = {k: ranged_part[k] for k in ranged_part}
            ss[opz[0]] = r
            rejected.append(ss)
    elif operation == "<":
        accepted_parts = get_overlapping_range(ranged_part[opz[0]][0], ranged_part[opz[0]][1], 1, int(opz[1])-1)
        if accepted_parts != None:
            ss = {k: ranged_part[k] for k in ranged_part}
            ss[opz[0]] = accepted_parts
            accepted.append((ss, rule[1]))
        rejected_parts = get_non_overlapping_ranges(ranged_part[opz[0]][0], ranged_part[opz[0]][1], 1, int(opz[1])-1)
        for r in rejected_parts:
            ss = {k: ranged_part[k] for k in ranged_part}
            ss[opz[0]] = r
            rejected.append(ss)
    return accepted, rejected

def split_workflow(ranged_part, workflow):
    next_ranges = []
    working_ranges = [ranged_part]
    for rule in workflow[0]:
        next_working_ranges = []
        for part in working_ranges:
            accepted, rejected = split_workflow_rule(part, rule)
            next_ranges.extend(accepted)
            next_working_ranges.extend(rejected)
        working_ranges = next_working_ranges
    for n in working_ranges:
        next_ranges.append((n, workflow[1]))
    return next_ranges

# def testing():
#     xxx = []
#     for i in range(10):
#         xxx.append(lambda x: x>i)
#     for i in range(15):
#         for x in range(10):
#             print(x > i, end= " ")
#             print(xxx[x](i), end=" ")
#             print( " -- ", end="")
#         print(i)
# testing()

def run(fname):
    lines = [line for line in open(fname, 'r').readlines()]
    f = open(fname, 'r').read().strip()
    r_workflows, r_parts = f.split("\n\n")
    workflows = {}
    parts = []
    for wf in r_workflows.splitlines():
        wf = wf.strip()
        key, content = wf.split("{")
        rules = content[:-1].split(",")
        compares = []
        for rule in rules[:-1]:
            # print(key, rule)
            op, target = rule.split(":")
            if ">" in op:
                opz = op.split(">")
                compares.append((lambda x,opz=opz: x[opz[0]] > int(opz[1]), target, opz, ">"))
            elif "<" in op:
                opz = op.split("<")
                compares.append((lambda x,opz=opz: x[opz[0]] < int(opz[1]), target, opz, "<"))
        workflows[key] = (compares, rules[-1])
    
    for p in r_parts.splitlines():
        pf = p.strip()
        pf = pf[1:]
        pf = pf[:-1]
        pf = pf.split(",")
        v_map = ["x", "m", "a", "s"]
        building = {}
        for k, v in enumerate(pf):
            v = v.split("=")
            building[v_map[k]] = int(v[1])
        parts.append(building)
    
    part1 = 0
    first_workflow = "in"
    for p in parts:
        cur_workflow = first_workflow
        while True:
            cur_workflow = eval_workflow(p, workflows[cur_workflow])
            # print(cur_workflow)
            if cur_workflow == "A":
                # print(p, cur_workflow)
                part1 += p["x"] + p["m"] + p["a"] + p["s"]
                break
            elif cur_workflow == "R":
                break
    # print(workflows["qs"])
    # print(workflows["qs"][0][0][0]({"x":3449}))

    part2 = 0
    ranges = [({"x":(1,PART_MAX),"m":(1,PART_MAX),"a":(1,PART_MAX),"s":(1,PART_MAX)}, first_workflow)]
    while True:
        next_ranges = []
        for r in ranges:
            ranged_part, wf = r
            # print(r)
            nr = split_workflow(ranged_part, workflows[wf])
            for val in nr:
                if val[1] == "A":
                    part2 += get_range_size(*val[0]["x"]) * get_range_size(*val[0]["m"]) * get_range_size(*val[0]["a"]) * get_range_size(*val[0]["s"])
                elif val[1] == "R":
                    pass
                else:
                    next_ranges.append(val)
        ranges = next_ranges
        if len(ranges) == 0:
            break

    print(f"part 1:")
    print(f"{part1}")

    print(f"part 2:")
    print(f"{part2}")

print("TEST")
run('inputs/test.txt')
print()
print("REAL")
run('inputs/day19.txt')