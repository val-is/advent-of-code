inputs = [i.strip() for i in open('inputs/day5.txt', 'r').readlines()]

# bit level hacking because it's FUN lmao
# it's completely useless, just me messing around

def calc_id(seat):
    row, col = seat
    return 8 * row + col

def conv_instr_bin(instructions):
    # convert instruction string to integer representation
    # FFBB --> 1100 --> 12 (endianness reverses it)
    # RLRR --> 1101 --> 11
    # [f, b] = [0, 1], [l, r] = [0, 1]
    row_dir = instructions[:7]
    col_dir = instructions[-3:]
    instruction = 0
    p = 1
    for v in row_dir + col_dir:
        if v == "B" or v == "R":
            instruction += p
        p = p << 1
    return instruction

def find_tree_loc(instr_int, length):
    # find position in the tree thingy
    mi = 0
    ma = 2**length
    p = 1
    for _ in range(length):
        mid = (mi + ma) / 2
        if p & instr_int:
            # take upper
            mi = mid
        else:
            ma = mid
        p = p << 1
    return mi

def get_location(instructions):
    int_instr = conv_instr_bin(instructions)
    row_instr =  int_instr & 0b0001111111
    col_instr = (int_instr & 0b1110000000) >> 7
    row = find_tree_loc(row_instr, 7)
    col = find_tree_loc(col_instr, 3)
    return (int(row), int(col))

ticket_ids = sorted([calc_id(get_location(ticket)) for ticket in inputs])
print(f"part 1: {max(ticket_ids)}")

for i, ticket in enumerate(ticket_ids[:-1]):
    if ticket_ids[i+1] - ticket == 2:
        print(f"part 2: {ticket+1}")
        break