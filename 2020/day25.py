inputs = [i.strip() for i in open('inputs/day25.txt', 'r').readlines()]

door_public, card_public = [*map(int, inputs)]

def transform(subject, loop):
    v = 1
    for _ in range(loop):
        v *= subject
        v %= 20201227
    return v

def brute_force_loop(subject, target):
    l = 1
    v = 1
    while True:
        v *= subject
        v %= 20201227
        if v == target:
            return l
        l += 1

def calculate_handshake(subject, loop_a, a_public, loop_b, b_public):
    key_a = transform(b_public, loop_a)
    key_b = transform(a_public, loop_b)
    assert key_a == key_b
    return key_a

loop_door = brute_force_loop(7, door_public)
loop_card = brute_force_loop(7, card_public)

part1 = calculate_handshake(7, loop_door, door_public, loop_card, card_public)
print(f"part 1: {part1}")

part2 = "there was no part 2. ggs"
print(f"part 2: {part2}")