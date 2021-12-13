inputs = open('inputs/day13.txt', 'r').read().strip()

a, b = inputs.split("\n\n")

dots = set()
for i in a.split("\n"):
    x, y = i.strip().split(",")
    dots.add((int(x), int(y)))

folds = []
for i in b.split("\n"):
    a, b = i[11:].strip().split('=')
    folds.append((a, int(b)))

def fold_up(dots, y):
    def trans_pos(y_in):
        if y_in < y:
            return y_in
        dist = y_in - y
        return y - dist
    new_dots = set()
    for d in dots:
        new_dots.add((d[0], trans_pos(d[1])))
    return new_dots

def fold_down(dots, x):
    def trans_pos(x_in):
        if x_in < x:
            return x_in
        dist = x_in - x
        return x - dist
    new_dots = set()
    for d in dots:
        new_dots.add((trans_pos(d[0]), d[1]))
    return new_dots

def apply_instr(dots, instr):
    if instr[0] == "y":
        return fold_up(dots, instr[1])
    if instr[0] == "x":
        return fold_down(dots, instr[1])

d = apply_instr(dots, folds[0])

part1 = len(d)
print(f"part 1: {part1}")

for i in folds:
    dots = apply_instr(dots, i)

def vis(dots):
    tiles = {}
    m_x  =0
    m_y = 0
    for i in dots:
        tiles[i] = True
        m_x = max(i[0], m_x)
        m_y = max(i[1], m_y)
    for y in range(m_y+1):
        s = ""
        for x in range(m_x+1):
            if (x, y) in tiles:
                s += "#"
            else:
                s += " "
        print(s)

vis(dots)
print(f"part 2: figure it out yourself ^^^ :P") 
