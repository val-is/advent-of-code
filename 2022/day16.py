import multiprocessing

lines = open("inputs/day16.txt", 'r').readlines()

MAX_TIME = 29

connections = {}
flow_rates = {}

for line in lines:
    spl = line.strip().split()
    valve = spl[1]
    flow_rate = spl[4]
    conns = spl[9:]

    flow_rate = int(flow_rate.split('=')[1][:-1])
    conns = [i[:-1] for i in conns[:-1]] + [conns[-1]]
    
    flow_rates[valve] = flow_rate
    connections[valve] = frozenset(conns)

relevant_nodes = {i for i in flow_rates if flow_rates[i] != 0} | {"AA"}
relevant_nodes = [*relevant_nodes]
relevant_mask_idx = {v: k for k, v in enumerate(relevant_nodes)}

# calculate adjacencies
adjacencies = {node: {other: None for other in relevant_nodes} for node in relevant_nodes}

def calc_best_adj(a, b, traversed=frozenset()):
    best_dist = 999
    if a == b:
        return 0
    for conn in connections[a]:
        if conn in traversed:
            continue
        best_dist = min(calc_best_adj(conn, b, traversed | frozenset({a}))+1, best_dist)
    return best_dist

for a in relevant_nodes:
    for b in relevant_nodes:
        adjacencies[a][b] = calc_best_adj(a, b, frozenset({a}))

# also it's better to only consider nonzero flow nodes for memoization (including AA)
# space should be 30min*15nodes*2^15 opened nodes
# mem addresses as [min][node][visited]
# opened can be a bitmask of 2**len(nonzero_nodes)
mem = {
    t: {
        node: {
            i: None for i in range(2**len(relevant_nodes))
        } for node in relevant_nodes
    } for t in range(30)
}

def get_pressure_releasing(opened):
    return sum(flow_rates[relevant_nodes[i]] for i in range(len(relevant_nodes)) if ((1<<i)&opened))


def solve(time, node, opened, pressure_released=0, MAX_TIME=MAX_TIME, nodes_ignoring=0):
    global mem
    
    if time > MAX_TIME:
        return 
    if mem[time][node][opened] != None and mem[time][node][opened] > pressure_released:
        return
    if time == MAX_TIME:
        if mem[time][node][opened] == None or pressure_released > mem[time][node][opened]:
            mem[time][node][opened] = pressure_released
        return

    for adj in adjacencies[node]:
        if ((1<<relevant_mask_idx[adj]) & opened) != 0 or ((1<<relevant_mask_idx[adj]) & nodes_ignoring) != 0:
            continue
        additional_released = 0
        dist = adjacencies[node][adj]
        if dist+1 >= MAX_TIME:
            continue
        additional_released += dist * get_pressure_releasing(opened)
        additional_released += get_pressure_releasing(opened | (1<<relevant_mask_idx[adj]))
        solve(time + dist + 1, adj, opened | (1<<relevant_mask_idx[adj]), pressure_released + additional_released, MAX_TIME, nodes_ignoring)
    solve(MAX_TIME, node, opened, pressure_released + (MAX_TIME-time) * get_pressure_releasing(opened), MAX_TIME, nodes_ignoring)
    mem[time][node][opened] = pressure_released


solve(0, "AA", 1<<relevant_mask_idx["AA"], 0)
max_final = 0
for v in mem[MAX_TIME]:
    for v2 in mem[MAX_TIME][v]:
        if mem[MAX_TIME][v][v2] != None:
            max_final = max(max_final, mem[MAX_TIME][v][v2])
print(f"part 1: {max_final}")

# part 2
# what if we dispatch the elephant everywhere we don't go?
# basically, find the two maximum memoized released pressures in which the opened valves have no overlap

base_dispatch = 1<<relevant_mask_idx["AA"]
best_p2 = 0
MAX_TIME_P2 = 25
solve(0, "AA", 1<<relevant_mask_idx["AA"], 0, MAX_TIME_P2)
p2_outcomes_flat = [*mem[MAX_TIME_P2].values()]
p2_outcomes = {
    opened: None for opened in range(2**len(relevant_nodes))
}
for v in p2_outcomes_flat:
    for opened in v:
        if p2_outcomes[opened] == None:
            p2_outcomes[opened] = v[opened]
        elif v[opened] != None and v[opened] > p2_outcomes[opened]:
            p2_outcomes[opened] = v[opened]
p2_outcomes = {k: p2_outcomes[k] for k in p2_outcomes if p2_outcomes[k] != None}

TOP_SLIDING_WINDOW = 100
top_values = [*zip(p2_outcomes.keys(), p2_outcomes.values())]
top_values = sorted(top_values, key=lambda x: x[1])[::-1]

for a in top_values[:TOP_SLIDING_WINDOW]:
    for b in top_values:
        if a[0] & b[0] != base_dispatch:
            continue
        best_p2 = max(best_p2, a[1]+b[1])
print(f"part 2: {best_p2}")