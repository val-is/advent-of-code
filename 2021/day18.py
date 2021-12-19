import math

inputs = open('inputs/day18.txt', 'r').readlines()

lines = []
for line in inputs:
    lines.append(eval(line)) # tehe :P

def attempt_explode(line):
    # leftmost pair == DFS
    pair_pos = -2
    def get_explode_pair(l, depth=0):
        # also remove/explode in place
        nonlocal pair_pos
        if type(l) != list:
            assert False
        a, b = l
        if type(a) == list:
            pair, delete = get_explode_pair(a, depth+1)
            if delete:
                l[0] = 0
            if pair != None:
                return pair, False
        else:
            pair_pos += 1
        if type(b) == list:
            pair, delete = get_explode_pair(b, depth+1)
            if delete:
                l[1] = 0
            if pair != None:
                return pair, False
        else:
            pair_pos += 1
        if depth >= 4:
            return [a,b], True
        return None, False
    
    pair, _ = get_explode_pair(line)
    if pair == None:
        return False

    a, b = pair
    
    # add pair components to things at pos
    def add_at_pos(l, target_pos, amount):
        cur_pos = 0
        def traverse_to_pos(l):
            nonlocal cur_pos
            if type(l) != list:
                assert False
            
            a, b = l
            if type(a) == list:
                traverse_to_pos(a)
            elif target_pos == cur_pos:
                l[0] += amount
                cur_pos += 1
            else:
                cur_pos += 1
            
            if type(b) == list:
                traverse_to_pos(b)
            elif target_pos == cur_pos:
                l[1] += amount
                cur_pos += 1
            else:
                cur_pos += 1
        traverse_to_pos(l)
    
    add_at_pos(line, pair_pos-1, a)
    add_at_pos(line, pair_pos+1, b)

    return True

def attempt_split(line):
    # DFS to first num >= 10, split it
    def split_inner(l):
        if type(l) != list:
            assert False
        a, b = l
        if type(a) == list:
            if split_inner(a):
                return True
        elif a >= 10:
            l[0] = [math.floor(a/2), math.ceil(a/2)]
            return True
        if type(b) == list:
            if split_inner(b):
                return True
        elif b >= 10:
            l[1] = [math.floor(b/2), math.ceil(b/2)]
            return True
        return False
    return split_inner(line)

def apply_reduction(line):
    if attempt_explode(line):
        return True

    if attempt_split(line):
        return True

    return False

def reduce_line(line):
    while True:
        reduced = apply_reduction(line)
        if not reduced:
            return

def sum_lines(a, b):
    return [a, b]

def magnitude(line):
    if type(line) != list:
        return line
    a, b = line
    return magnitude(a) * 3 + magnitude(b) * 2

s = lines[0]
for i in lines[1:]:
    s = sum_lines(s, i)
    reduce_line(s)

part1 = magnitude(s)
print(f"part 1: {part1}")

max_mag = 0

for k1, _ in enumerate(inputs):
    for k2, _ in enumerate(inputs):
        v1 = eval(inputs[k1])
        v2 = eval(inputs[k2])
        s = sum_lines(v1, v2)
        reduce_line(s)
        mag = magnitude(s)
        max_mag = max(max_mag, mag)

part2 = max_mag
print(f"part 2: {part2}")
