inputs = open("inputs/day23.txt", 'r').read().strip()
initial_cups = [*map(int, inputs)]

def parse_dll(cups):
    dll = [[
        k-1 if k-1 >= 0 else len(cups)-1,
        v,
        k+1 if k+1 < len(cups) else 0] for k, v in enumerate(cups)]
    return dll

def move(cups, cup_positions, current_index, n_cups):
    _, cur_val, follow_index = cups[current_index]
    following = []
    for _ in range(3):
        following.append(follow_index)
        _, _, follow_index = cups[follow_index]
    cups[current_index][2], cups[follow_index][0] = follow_index, current_index

    n = 1
    dest_index = following[0]
    while dest_index in following:
        searching_val = (cur_val-n) % (n_cups+1)
        if searching_val <= 0:
            searching_val = n_cups
        dest_index = cup_positions[searching_val]
        n += 1

    next_cup = cups[dest_index][2]
    cups[following[0]][0], cups[dest_index][2] = dest_index, following[0]
    cups[following[-1]][2], cups[next_cup][0]= next_cup, following[-1]
    return cups[cup_positions[cur_val]][2]

def play_game(cups_base, n_cups, n_turns):
    cups = cups_base.copy()
    cups += [*range(max(cups)+1, n_cups+1)]
    cup_positions = {v: k for k, v in enumerate(cups)}
    cups = parse_dll(cups)
    cur_index = 0
    for _ in range(n_turns):
        cur_index = move(cups, cup_positions, cur_index, n_cups)
    return cups, cup_positions

part_1, part_1_pos = play_game(initial_cups, 9, 100)
init = index = part_1_pos[1]
s = ""
while True:
    if index == init and s != "":
        break
    _, v, index = part_1[index]
    s += str(v)
print(f"part 1: {s[1:]}")

part_2, part_2_pos = play_game(initial_cups, 1_000_000, 10_000_000)
acc = 1
index = part_2_pos[1]
for _ in range(2):
    index = part_2[index][2]
    acc *= part_2[index][1]
print(f"part 2: {acc}")
