data_raw = open('inputs/day2.txt', 'r').readlines()
boxes = []
for i in data_raw:
    l, w, h = [int(j) for j in i.strip().split('x')]
    boxes += [(l, w, h)]

def calc_paper(sides):
    l, w, h = sides
    a, b, c = [l*w, w*h, h*l]
    return 2*a + 2*b + 2*c + min(a, b, c)

p1 = sum([calc_paper(box) for box in boxes])
print(f"part 1: {p1}")

def calc_ribbon(sides):
    l, w, h = sides
    bow = l*w*h
    a, b, c = l+w, w+h, h+l
    return bow + min(2*a, 2*b, 2*c)

p2 = sum([calc_ribbon(box) for box in boxes])
print(f"part 2: {p2}")