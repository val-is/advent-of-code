import sys
# sys.setrecursionlimit(15000)

def run(fname):
    lines = [line for line in open(fname, 'r').readlines()]

    conns = {}
    states = {}
    inputs = {}
    for line in lines:
        a, b = line.strip().split(" -> ")
        if a.startswith("broadcaster"):
            mod_type = "B"
            mod_name = a
        else:
            mod_type = a[0]
            mod_name = a[1:]
        outputs = [i for i in b.split(", ")]
        conns[mod_name] = (mod_type, outputs)
        for o in outputs:
            if o in inputs:
                inputs[o].append(mod_name)
            else:
                inputs[o] = [mod_name]
        if mod_type == "%":
            states[mod_name] = False
        # elif mod_type == "&":
        #     states[mod_name] = {k: False for k in outputs}
    for m in conns:
        if conns[m][0] == "&":
            states[m] = {k: False for k in inputs[m]}
    conns["output"] = ("%", [])
    states["output"] = False

    cycles = {}

    lows = 0
    highs = 0

    i = 0
    done = False
    ww = ["ln", "dr", "zx", "vn"]
    ww_cycles = {k: None for k in ww}
    while not done:
        for k in ww_cycles:
            if ww_cycles[k] == None:
                break
        else:
            print(ww_cycles, states)
            return

        state_bm = 0
        k = 0
        for s in states:
            if conns[s][0] == "%":
                state_bm |= (1 if states[s] else 0) << k
            k+=1
        if state_bm != 0:
            if state_bm in cycles:
                cycles[state_bm].append(i)
            else:
                cycles[state_bm] = [i]
            for state in cycles:
                if state & state_bm == state and state_bm != state:
                    cycles[state].append(i)
                    if len(cycles[state])==5 and cycles[state][1]-cycles[state][0] == 2048:
                        print(i, cycles[state], state&state_bm, cycles[state][1]-cycles[state][0])

        i+=1
        # print(i)
        start_module = "broadcaster"
        update_queue = [("broadcaster", False, "")]
        while len(update_queue) > 0:
            u = update_queue.pop(0)
            current, value, sent_by = u
            if current == "rx" and value == False:
                done = True
                break
            # if value:
            #     highs += 1
            # else:
            #     lows += 1
            if current not in conns:
                continue
            target_type, target_outputs = conns[current]
            if target_type == "B":
                for target in target_outputs:
                    update_queue.append((target, value, current))
            elif target_type == "%":
                if value:
                    pass
                else:
                    states[current] = not states[current]
                    out = states[current]
                    for target in target_outputs:
                        update_queue.append((target, out, current))
            elif target_type == "&":
                states[current][sent_by] = value
                a = True
                for k in states[current]:
                    a = a and states[current][k]
                for target in target_outputs:
                    update_queue.append((target, not a, current))
                if current in ww and (not a):
                    if ww_cycles[current] == None:
                        ww_cycles[current] = i

    part1 = highs*lows
    part2 = i
    
    print(f"part 1:")
    print(f"{part1}")

    print(f"part 2:")
    print(f"{part2}")

# print("TEST")
# run('inputs/test.txt')
# print()
print("REAL")
run('inputs/day20.txt')