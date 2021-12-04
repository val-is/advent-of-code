inputs = open('inputs/day04.txt', 'r').read().split("\n\n")

draws = [int(i) for i in inputs[0].split(",")]

raw_board_maps = []
boards_raw = inputs[1:]
for b in boards_raw:
    tiles = {}
    for y, row in enumerate(b.strip().split("\n")):
        for x, val in enumerate(row.strip().split()):
            val = int(val)
            tiles[(x, y)] = val
    raw_board_maps.append(tiles)

BOARD_SIZE = 5

def get_board_struct(board):
    new_board = {}
    for tile in board:
        new_board[tile] = (board[tile], False)
    return new_board

def fill_tiles(board, val_to_fill):
    for tile in board:
        val, _ = board[tile]
        if val == val_to_fill:
            board[tile] = (val, True)
    return board

def check_row_filled(board, y):
    for x in range(BOARD_SIZE):
        _, filled = board[(x, y)]
        if not filled:
            return False
    return True

def check_col_filled(board, x):
    for y in range(BOARD_SIZE):
        _, filled = board[(x, y)]
        if not filled:
            return False
    return True

def check_for_win(board):
    for y in range(BOARD_SIZE):
        if check_row_filled(board, y):
            return True
    for x in range(BOARD_SIZE):
        if check_col_filled(board, x):
            return True
    return False

def score_board(board):
    s = 0
    for tile in board:
        val, filled = board[tile]
        if not filled:
            s += val
    return s

def p1(raw_board_maps):
    boards = []
    for board_raw in raw_board_maps:
        boards.append(get_board_struct(board_raw))

    for draw in draws:
        for b in boards:
            fill_tiles(b, draw)
        for b in boards:
            if check_for_win(b):
                return draw * score_board(b)
    return -1

part1 = p1(raw_board_maps)
print(f"part 1: {part1}")

def p2(raw_board_maps):
    boards = []
    for board_raw in raw_board_maps:
        boards.append(get_board_struct(board_raw))

    for draw in draws:
        for b in boards:
            fill_tiles(b, draw)
        indexes_removing = []
        for index, b in enumerate(boards):
            if check_for_win(b):
                if len(boards) == 1:
                    return draw * score_board(b)
                indexes_removing.append(index)
        for i in sorted(indexes_removing)[::-1]:
            boards.pop(i)
    return -1

part2 = p2(raw_board_maps)
print(f"part 2: {part2}")
