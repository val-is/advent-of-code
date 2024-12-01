import sys
sys.setrecursionlimit(3000)

def get_cut_wires(wires, cutting=[]):
    wires_2 = {k: wires[k].copy() for k in wires}
    for c in cutting:
        c = list(c)
        wires_2[c[0]].remove(c[1])
        wires_2[c[1]].remove(c[0])
    return wires_2

def get_inner_parts(wires):
    big_groups = []
    for w in wires:
        w_set = wires[w]
        groups_adding = []
        groups_disjoing = []
        for group in big_groups:
            if len(w_set & group) != 0:
                groups_adding.append(group)
            else:
                groups_disjoing.append(group)
        new_big_groups = []
        s = w_set.copy()
        for g in groups_adding:
            s |= g
        new_big_groups.append(s)
        for g in groups_disjoing:
            new_big_groups.append(g)
        big_groups = new_big_groups

    return big_groups

DP = {}
def get_cutting_groups(wires, cutting:frozenset, prev_cuts:frozenset=frozenset()):
    global DP
    dpkey = frozenset((cutting, prev_cuts))
    if dpkey in DP:
        cc,n_to_cut,n_prev_cuts = DP[dpkey]
    else:
        lc = list(cutting)
        cutting_now = lc[0]
        if len(lc) > 1:
            cutting_later = lc[1:]
        else:
            cutting_later = []
        cc = get_cut_wires(wires, [cutting_now])
        n_to_cut = frozenset(cutting_later)
        n_prev_cuts = frozenset(prev_cuts | {cutting_now})
        DP[dpkey] = (cc, n_to_cut, n_prev_cuts)
    if len(n_to_cut) > 0:
        return get_cutting_groups(cc, n_to_cut, n_prev_cuts)
    else:
        return cc

def run(fname):
    global DP
    DP = {}
    lines = [line for line in open(fname, 'r').readlines()]

    wires = {}
    www = set()
    for line in lines:
        a, b = line.strip().split(": ")
        wires[a] = set(b.split(" "))
        www |= {a} | wires[a]

    for k in www:
        if k not in wires:
            wires[k] = set()

    for k in wires:
        for v in wires[k]:
            wires[v] |= {k}

    # o = open("tmp.txt", 'w')
    # for k in wires:
    #     for k2 in wires[k]:
    #         o.write(f"{k}->{k2};\n")
    # o.close()
            
    from networkx import Graph, minimum_edge_cut, connected_components
    nodes = set()
    edges = set()
    for w in wires:
        nodes.add(w)
        for w2 in wires[w]:
            edges.add((w, w2))
    G = Graph()
    G.add_nodes_from(nodes)
    G.add_edges_from(edges)
    edges_to_cut = minimum_edge_cut(G)
    for edge in edges_to_cut:
        G.remove_edge(*edge)
    c = [len(c) for c in connected_components(G)]
    print(c)
    return

    cut_groups = []

    for a1 in wires:
        for a2 in wires[a1]:
            for b1 in wires:
                for b2 in wires[b1]:
                    for c1 in wires:
                        for c2 in wires[c1]:
                            a = frozenset((a1, a2))
                            b = frozenset((b1, b2))
                            c = frozenset((c1, c2))
                            if a == b or b == c or c == a:
                                continue
                            try:
                                w = get_cutting_groups(wires, frozenset((a, b, c)))
                                g = get_inner_parts(w)
                                if len(g) == 2:
                                    print(len(g[0]) * len(g[1]))
                                    return
                                    break
                            except KeyError:
                                pass
                            print(len(DP))
    # print(wires)
    # w = get_cut_wires(wires, [["hfx", "pzl"],["bvb","cmg"],["nvd","jqt"]])
    # g = get_inner_parts(w)
    # if len(g) == 2:
    #     print(len(g[0]) * len(g[1]))


    part1 = 0
    part2 = 0

    print(f"part 1:")
    print(f"{part1}")

    print(f"part 2:")
    print(f"{part2}")

print("TEST")
run('inputs/test.txt')
print()
print("REAL")
run('inputs/day25.txt')