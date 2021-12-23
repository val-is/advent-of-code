inputs = open('inputs/day23.txt', 'r').readlines()

start_tiles = {}

WAITING_TILES = [(i,1) for i in [1,2,4,6,8,10,11]]

ROOM_TILES = [
        (3,2),(3,3),(3,4),(3,5),
        (5,2),(5,3),(5,4),(5,5),
        (7,2),(7,3),(7,4),(7,5),
        (9,2),(9,3),(9,4),(9,5)
        ]

A_ROOM_TILES = [i for i in ROOM_TILES if i[1] == 2]
B_ROOM_TILES = [i for i in ROOM_TILES if i[1] == 3]
C_ROOM_TILES = [i for i in ROOM_TILES if i[1] == 4]
D_ROOM_TILES = [i for i in ROOM_TILES if i[1] == 5]
ROOMS = {(3,2): "A", (3,3): "A", (3,4): "A", (3,5): "A",
        (5,2): "B", (5,3): "B", (5,4): "B", (5,5): "B",
        (7,2): "C", (7,3): "C", (7,4): "C", (7,5): "C",
        (9,2): "D", (9,3): "D", (9,4): "D", (9,5): "D"
        }
COSTMAP = {"A":1,"B":10,"C":100,"D":1000}

waiting_tiles = {i: " " for i in WAITING_TILES}
start_tiles = {i: " " for i in ROOM_TILES}
for y, row in enumerate(inputs):
    for x, val in enumerate(row.rstrip("\n")):
        if val not in "ABCD":
            continue
        if (x, y) in ROOM_TILES:
            start_tiles[x, y] = val
        if (x, y) in WAITING_TILES:
            waiting_tiles[x, y] = val

def check_complete(room_tiles):
    cnt = 0
    for tile in room_tiles:
        if room_tiles[tile] != ROOMS[tile] and room_tiles[tile] != " ":
            return False
        if room_tiles[tile] in "ABCD":
            cnt += 1
    return cnt == 16

def serialize_state(room_pods, waiting_pods):
    r = tuple([(tile, room_pods[tile]) for tile in room_pods])
    w = tuple([(tile, waiting_pods[tile]) for tile in waiting_pods])
    return r, w

def get_possible_waiting_tiles(tile, waiting_pods):
    # tile, dist_horiz
    possible_l = [i for i in WAITING_TILES if i[0] < tile[0]]
    filled_l = [i for i in waiting_pods if i[0] < tile[0] and waiting_pods[i] != " "]
    possible_l = sorted(possible_l, key=lambda x: x[0])[::-1]
    ls = []
    for i in possible_l:
        if i not in filled_l:
            ls.append(i)
        else:
            break

    possible_r = [i for i in WAITING_TILES if i[0] > tile[0]]
    filled_r = [i for i in waiting_pods if i[0] > tile[0] and waiting_pods[i] != " "]
    possible_r = sorted(possible_r, key=lambda x: x[0])
    rs = []
    for i in possible_r:
        if i not in filled_r:
            rs.append(i)
        else:
            break

    possible = ls + rs
    r = []
    for i in possible:
        r.append((i, abs(tile[0] - i[0])))

    return r

def can_enter_home(tile, pod, room_pods, waiting_pods):
    # None or (tile, dist_horiz+depth)
    pod_room = [i for i in ROOMS if ROOMS[i] == pod]
    empty_in_room = []
    filled_in_room = []
    for i in pod_room:
        if room_pods[i] != pod and room_pods[i] != " ":
            return None, None
        elif room_pods[i] == " ":
            empty_in_room.append(i)
        else:
            filled_in_room.append(i)
    for i in filled_in_room:
        empty_in_room = [j for j in empty_in_room if j[1] < i[1]]
    if len(empty_in_room) == 0:
        return None, None
    target = sorted(empty_in_room, key=lambda x:x[1])[-1]
    dist = abs(target[0]-tile[0])+(target[1]-1)
    return target, dist

def cp(t):
    return {k: t[k] for k in t}

state_costs = {}
def iter(room_tiles, waiting_tiles, prev_states):
    serialized_state = serialize_state(room_tiles, waiting_tiles)
    if serialized_state in state_costs:
        return state_costs[serialized_state]

    if check_complete(room_tiles):
        return 0, True

    next_possible_states = [] # room, waiting, cost
    
    for k in A_ROOM_TILES:
        if room_tiles[k] == " ":
            continue
        
        # TODO repeat below
        # if lower tiles are happy and this one is too, we can skip
        
        if room_tiles[k[0], 3] == ROOMS[k[0], 3] \
                and room_tiles[k[0], 4] == ROOMS[k[0], 4] \
                and room_tiles[k[0], 5] == ROOMS[k[0], 5] \
                and room_tiles[k] == ROOMS[k]:
            continue

        # if room_tiles[k] == ROOMS[k]:
        #     continue
        
        target, dist = can_enter_home(k, room_tiles[k], room_tiles, waiting_tiles)
        if target != None:
            mi, ma = min(target[0], k[0]), max(target[0], k[0])
            can_move = True
            for i in waiting_tiles:
                if waiting_tiles[i] == " ":
                    continue
                if mi < i[0] < ma:
                    can_move = False
                    break
            if can_move:
                n_room, n_wait = cp(room_tiles), cp(waiting_tiles)
                n_room[target] = room_tiles[k]
                n_room[k] = " "
                next_possible_states.append((n_room, n_wait, (dist+1)*COSTMAP[room_tiles[k]]))
                continue  # always most optimal
        
        for waiting in get_possible_waiting_tiles(k, waiting_tiles):
            tile, dist = waiting
            n_room, n_wait = cp(room_tiles), cp(waiting_tiles)
            n_wait[tile] = room_tiles[k]
            n_room[k] = " "
            next_possible_states.append((n_room, n_wait, (dist+1)*COSTMAP[room_tiles[k]]))
    
    for k in B_ROOM_TILES:
        if room_tiles[k] == " ":
            continue
        
        # TODO repeat below
        if room_tiles[k[0], 2] != " ":
            continue
        
        # TODO repeat below
        # if lower tiles are happy and this one is too, we can skip
        if room_tiles[k[0], 4] == ROOMS[k[0], 4] \
                and room_tiles[k[0], 5] == ROOMS[k[0], 5] \
                and room_tiles[k] == ROOMS[k]:
            continue

        # if room_tiles[k] == ROOMS[k]:
        #     continue
        
        target, dist = can_enter_home(k, room_tiles[k], room_tiles, waiting_tiles)
        if target != None:
            mi, ma = min(target[0], k[0]), max(target[0], k[0])
            can_move = True
            for i in waiting_tiles:
                if waiting_tiles[i] == " ":
                    continue
                if mi < i[0] < ma:
                    can_move = False
                    break
            if can_move:
                n_room, n_wait = cp(room_tiles), cp(waiting_tiles)
                n_room[target] = room_tiles[k]
                n_room[k] = " "
                next_possible_states.append((n_room, n_wait, (dist+2)*COSTMAP[room_tiles[k]]))
                continue  # always most optimal
        
        for waiting in get_possible_waiting_tiles(k, waiting_tiles):
            tile, dist = waiting
            n_room, n_wait = cp(room_tiles), cp(waiting_tiles)
            n_wait[tile] = room_tiles[k]
            n_room[k] = " "
            next_possible_states.append((n_room, n_wait, (dist+2)*COSTMAP[room_tiles[k]]))
    
    for k in C_ROOM_TILES:
        if room_tiles[k] == " ":
            continue
        
        # TODO repeat below
        if room_tiles[k[0], 2] != " " or room_tiles[k[0], 3] != " ":
            continue
        
        # TODO repeat below
        # if lower tiles are happy and this one is too, we can skip
        if room_tiles[k[0], 5] == ROOMS[k[0], 5] \
                and room_tiles[k] == ROOMS[k]:
            continue

        # if room_tiles[k] == ROOMS[k]:
        #     continue
        
        target, dist = can_enter_home(k, room_tiles[k], room_tiles, waiting_tiles)
        if target != None:
            mi, ma = min(target[0], k[0]), max(target[0], k[0])
            can_move = True
            for i in waiting_tiles:
                if waiting_tiles[i] == " ":
                    continue
                if mi < i[0] < ma:
                    can_move = False
                    break
            if can_move:
                n_room, n_wait = cp(room_tiles), cp(waiting_tiles)
                n_room[target] = room_tiles[k]
                n_room[k] = " "
                next_possible_states.append((n_room, n_wait, (dist+3)*COSTMAP[room_tiles[k]]))
                continue  # always most optimal
        
        for waiting in get_possible_waiting_tiles(k, waiting_tiles):
            tile, dist = waiting
            n_room, n_wait = cp(room_tiles), cp(waiting_tiles)
            n_wait[tile] = room_tiles[k]
            n_room[k] = " "
            next_possible_states.append((n_room, n_wait, (dist+3)*COSTMAP[room_tiles[k]]))

    for k in D_ROOM_TILES:
        if room_tiles[k] == " ":
            continue
        
        # TODO repeat below
        if room_tiles[k[0], 2] != " " or room_tiles[k[0], 3] != " " or room_tiles[k[0], 4] != " ":
            continue
        
        # TODO repeat below
        # if lower tiles are happy and this one is too, we can skip
        if room_tiles[k] == ROOMS[k]:
            continue

        # if room_tiles[k] == ROOMS[k]:
        #     continue
        
        target, dist = can_enter_home(k, room_tiles[k], room_tiles, waiting_tiles)
        if target != None:
            mi, ma = min(target[0], k[0]), max(target[0], k[0])
            can_move = True
            for i in waiting_tiles:
                if waiting_tiles[i] == " ":
                    continue
                if mi < i[0] < ma:
                    can_move = False
                    break
            if can_move:
                n_room, n_wait = cp(room_tiles), cp(waiting_tiles)
                n_room[target] = room_tiles[k]
                n_room[k] = " "
                next_possible_states.append((n_room, n_wait, (dist+4)*COSTMAP[room_tiles[k]]))
                continue  # always most optimal
        
        for waiting in get_possible_waiting_tiles(k, waiting_tiles):
            tile, dist = waiting
            n_room, n_wait = cp(room_tiles), cp(waiting_tiles)
            n_wait[tile] = room_tiles[k]
            n_room[k] = " "
            next_possible_states.append((n_room, n_wait, (dist+4)*COSTMAP[room_tiles[k]]))

    for k in WAITING_TILES:
        if waiting_tiles[k] == " ":
            continue
        
        target, dist = can_enter_home(k, waiting_tiles[k], room_tiles, waiting_tiles)
        if target != None:
            mi, ma = min(target[0], k[0]), max(target[0], k[0])
            can_move = True
            for i in [j for j in waiting_tiles if j != k]:
                if waiting_tiles[i] == " ":
                    continue
                if mi < i[0] < ma:
                    can_move = False
                    break
            if can_move:
                n_room, n_wait = cp(room_tiles), cp(waiting_tiles)
                n_room[target] = waiting_tiles[k]
                n_wait[k] = " "
                next_possible_states.append((n_room, n_wait, (dist)*COSTMAP[waiting_tiles[k]]))
                continue  # can only move into room after waiting

    solved_costs = []

    for state in next_possible_states:
        n_room, n_wait, cost = state
        serialized = serialize_state(n_room, n_wait)
        if serialized in prev_states:
            continue
        n_prev = [*prev_states]
        n_prev.append(serialized)
        c, solved = iter(n_room, n_wait, n_prev)
        if solved:
            solved_costs.append(c+cost)

    if len(solved_costs) == 0:
        state_costs[serialized_state] = (0, False)
        return 0, False

    min_cost = min(solved_costs)

    state_costs[serialized_state] = (min_cost, True)

    return min_cost, True

part1 = iter(start_tiles, waiting_tiles, [])
print(f"part 1: {part1}")

part2 = 0
print(f"part 2: {part2}")
