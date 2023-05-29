inputs = open('inputs/day17.txt', 'r').read().strip()

shapes = [
    {(0,0), (1,0), (2,0), (3,0)},
    {(1,0), (0,-1), (1,-1), (2,-1), (1,-2)} ,
    {(0,0), (1,0), (2,0), (2,-1), (2,-2)} ,
    {(0,0), (0,-1), (0,-2), (0,-3)} ,
    {(0,0), (1,0), (0,-1), (1,-1)} ,
]


def print_grid(filled_blocks):
    ys = [i[1] for i in filled_blocks]
    mi_y, ma_y = min(ys), max(ys)
    for y in range(mi_y, ma_y+1):
        row = "|"
        for x in range(0, 7):
            if (x, y) in filled_blocks:
                row += "#"
            else:
                row += "."
        print(row + "|")
    print("+-------+")
    print()

def get_shape_filled(shape, position):
    return {(i[0]+position[0], i[1]+position[1]) for i in shape}

def check_collision(filled_block_spots, filled_rows):
    # return (block_col, wall_col)
    for piece in filled_block_spots:
        if piece[0] < 0 or piece[0] >= 7:
            return False, True
        # special case for hitting ground
        if piece[1] >= 0:
            return True, False
    if len(filled_block_spots & filled_rows) != 0:
        return True, False
    return False, False

def attempt_move_block(shape, pos, filled_rows, movement):
    # returns (done moving, filled_rows, new position)
    if movement == ".":
        # use to indicate soft drop
        shape_pos = get_shape_filled(shape, (pos[0], pos[1]+1))
        block_coll, wall_coll = check_collision(shape_pos, filled_rows)
        if block_coll:
            # lock in place before movement
            return True, filled_rows | get_shape_filled(shape, pos), pos
        assert not wall_coll
        return False, filled_rows, (pos[0], pos[1]+1)
    
    next_pos = None
    if movement == "<":
        next_pos = (pos[0]-1, pos[1])
    elif movement == ">":
        next_pos = (pos[0]+1, pos[1])
    shape_pos = get_shape_filled(shape, next_pos)
    
    block_coll, wall_coll = check_collision(shape_pos, filled_rows)
    if wall_coll or block_coll:
        # just don't move the block
        return False, filled_rows, pos
    else:
        # move the block
        return False, filled_rows, next_pos


def insert_new_block(shape, top_row_val, instruction_tape, instruction_pointer, filled_rows):
    # returns (updated filled_rows set, instr_pointer)
    cur_pos = (2, top_row_val-4)
    moving = True
    moves_done = 0
    # print("starting drop:")
    # print_grid(filled_rows | get_shape_filled(shape, cur_pos))
    while moving:
        cur_instr = instruction_tape[instruction_pointer]

        _, _, new_pos = attempt_move_block(shape, cur_pos, filled_rows, cur_instr)
        cur_pos = new_pos
        moves_done += 1
        # print(f"instr: {cur_instr}")
        # print_grid(filled_rows | get_shape_filled(shape, cur_pos))

        done, updated_filled_rows, new_pos = attempt_move_block(shape, cur_pos, filled_rows, ".")
        if done:
            filled_rows = updated_filled_rows
            moving = False
        else:
            cur_pos = new_pos
        # print(f"dropping: ")
        # print_grid(filled_rows | get_shape_filled(shape, cur_pos))

        instruction_pointer += 1 
        instruction_pointer %= len(instruction_tape)

    # print_grid(filled_rows | get_shape_filled(shape, cur_pos))
    return (filled_rows | get_shape_filled(shape, cur_pos)), instruction_pointer, moves_done

TOP_LOOKING = 75

def run_for_iters(iters):
    # main loop
    instruction_pointer = 0
    top_row_val = 0 # at the start
    filled_blocks = set()
    for i in range(iters):
        shape_dropping = shapes[i%len(shapes)]
        
        filled_blocks, instruction_pointer, _ = insert_new_block(shape_dropping, top_row_val, inputs, instruction_pointer, filled_blocks)

        top_row_val = min([i[1] for i in filled_blocks])

        new_filled_blocks = set()
        for block in filled_blocks:
            if block[1] < top_row_val + TOP_LOOKING:
                new_filled_blocks.add(block)
        filled_blocks = new_filled_blocks
        
        # print(f"block {i}")
        # print_grid(filled_blocks)
    return top_row_val

part_1 = -run_for_iters(2022)
print(f"part 1: {part_1}")