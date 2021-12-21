inputs = open('inputs/day21.txt', 'r').readlines()

init_a, init_b = [int(inputs[i][28:].strip()) for i in [0, 1]]

pos_a = init_a
pos_b = init_b

score_a = 0
score_b = 0

roll = 1
rs = 0
def get_roll():
    global rs
    global roll
    rs += 1
    r =  roll
    roll += 1
    if roll > 100:
        roll = 1
    return r

while score_a < 1000 and score_b < 1000:
# for _ in range(2):
    a, b, c = [get_roll() for _ in range(3)]
    d = sum([a,b,c])
    pos_a += d
    while pos_a > 10:
        pos_a -= 10
    score_a += pos_a
    if score_a >= 1000:
        break
    
    a, b, c = [get_roll() for _ in range(3)]
    d = sum([a,b,c])
    pos_b += d
    while pos_b > 10:
        pos_b -= 10
    score_b += pos_b

part1 = min(score_a, score_b) * rs
print(f"part 1: {part1}")

from toolbox import memoize_the_world as za_warudo
from itertools import product

@za_warudo
def step(pos_a, pos_b, score_a, score_b, player=1):
    wins_a = 0
    wins_b = 0

    for roll in [sum(i) for i in product([1,2,3],repeat=3)]:
        new_pos_a = pos_a
        new_pos_b = pos_b
        new_score_a = score_a
        new_score_b = score_b

        if player == 1:
            new_pos_a = roll + pos_a
            while new_pos_a > 10:
                new_pos_a -= 10
            new_score_a = new_pos_a + score_a
            if new_score_a >= 21:
                wins_a += 1
                continue
        
        if player == 2:
            new_pos_b = roll + pos_b
            while new_pos_b > 10:
                new_pos_b -= 10
            new_score_b = new_pos_b + score_b
            if new_score_b >= 21:
                wins_b += 1
                continue
        
        a, b = step(new_pos_a, new_pos_b, new_score_a, new_score_b, 2 if player == 1 else 1)
        wins_a += a
        wins_b += b
    
    return wins_a, wins_b

part2 = max([*step(init_a,init_b,0,0)])
print(f"part 2: {part2}")
