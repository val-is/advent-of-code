import hashlib

key = open('inputs/day4.txt', 'r').read()

def test_num(i):
    h = hashlib.md5(f"{key}{i}".encode()).hexdigest()
    return h[:5] == '00000'

i = 0
while True:
    if test_num(i):
        break
    i += 1
print(f"part 1: {i}")

# haha just throwing my computer at it go brrrr

def test_num_p2(i):
    h = hashlib.md5(f"{key}{i}".encode()).hexdigest()
    return h[:6] == '000000'

i = 0
while True:
    if test_num_p2(i):
        break
    i += 1
print(f"part 2: {i}")