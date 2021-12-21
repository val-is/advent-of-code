inputs = open('inputs/day20.txt', 'r').readlines()

alignment, image = inputs[0], inputs[2:]
alignment = alignment.strip()

orig = {}
for y, row in enumerate(image):
    for x, val in enumerate(row.strip()):
        orig[x, y] = True if val == "#" else False

def get_kern(pos):
    x, y = pos
    s = [
            (x-1, y-1),
            (x, y-1),
            (x+1, y-1),
            (x-1, y),
            (x, y),
            (x+1, y),
            (x-1, y+1),
            (x, y+1),
            (x+1, y+1),
            ]
    return s

def kernalize(image, pos, alignment, default):
    i = 0
    for adj in get_kern(pos):
        i = i << 1
        if adj not in image:
            i += 1 if default else 0
            continue
        if image[adj]:
            i += 1
    return alignment[i] == "#"

def get_bounds(image):
    minx, miny = None, None
    maxx, maxy = None, None
    for k in image:
        x, y = k
        if minx == None:
            minx, maxx = x, x
            miny, maxy = y, y
            continue
        minx = min(x, minx)
        miny = min(y, miny)
        maxx = max(x, maxx)
        maxy = max(y, maxy)
    return (minx, miny), (maxx, maxy)

def update_image(image, alignment, default=False):
    new_img = {}
    a, b = get_bounds(image)
    for x in range(a[0]-5, b[0]+5):
        for y in range(a[1]-5, b[1]+5):
            new_img[x, y] = kernalize(image, (x, y), alignment, default)
    return new_img

def count_pix(image):
    s = 0
    for i in image:
        if image[i]:
            s += 1
    return s

def print_img(image):
    a, b = get_bounds(image)
    for y in range(a[1], b[1]+1):
        s = ""
        for x in range(a[0], b[0]+1):
            s += "#" if image[x, y] else "."
        print(s)

image = orig

b = False
for _ in range(2):
    image = update_image(image, alignment, b)
    b = not b

part1 = count_pix(image)
print(f"part 1: {part1}")

image = orig

b = False
for _ in range(50):
    image = update_image(image, alignment, b)
    b = not b

part2 = count_pix(image)
print(f"part 2: {part2}")
