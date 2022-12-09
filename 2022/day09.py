import math

inputs = [i.strip() for i in open('inputs/day09.txt', 'r').readlines()]

instrs = []
for i in inputs:
    a, b = i.split()
    instrs.append((a, int(b)))

deltas = {
    'U': [0, 1],
    'D': [0, -1],
    'L': [-1, 0],
    'R': [1, 0],
}

def step(head, tail):
    dx, dy = (head[0]-tail[0], head[1]-tail[1])
    if dx != 0 and dy != 0 and (abs(dx) >= 2 or abs(dy) >= 2):
        tail = (tail[0]+math.copysign(1, dx), tail[1]+math.copysign(1, dy))
    elif abs(dx) >= 2 and dy == 0:
        tail = (tail[0]+math.copysign(1,dx), tail[1])
    elif abs(dy) >= 2 and dx == 0:
        tail = (tail[0], tail[1]+math.copysign(1,dy))
    tail = (int(tail[0]),int(tail[1]))
    return tail

def run_p1(instrs):
    visited = set()
    head = (0, 0)
    tail = (0, 0)
    for dir, steps in instrs:
        dx, dy = deltas[dir]
        for _ in range(steps):
            head = (head[0]+dx, head[1]+dy)
            tail = step(head, tail)
            visited.add(tail)
    return len(visited)

part1 = run_p1(instrs)
print(f"part 1: {part1}")

def run_p2(instrs):
    visited = set()
    head = (0, 0)
    rope = [(0, 0) for _ in range(9)]
    for dir, steps in instrs:
        dx, dy = deltas[dir]
        for _ in range(steps):
            head = (head[0]+dx, head[1]+dy)
            for idx in range(len(rope)):
                if idx == 0:
                    rope_head, rope_tail = head, rope[idx]
                else:
                    rope_head, rope_tail = rope[idx-1], rope[idx]
                rope[idx] = step(rope_head, rope_tail)
            visited.add(rope[-1])
    return len(visited)

part2 = run_p2(instrs)
print(f"part 2: {part2}")