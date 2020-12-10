from toolbox import memoize

inputs = [int(i) for i in open('inputs/day10.txt', 'r').readlines()]
inputs = sorted(inputs)

inputs += [max(inputs) + 3]
d1 = 0
d3 = 0
for i in range(len(inputs)):
    if i == 0:
        diff = inputs[i]
    else:
        diff = inputs[i] - inputs[i-1]
    if diff == 1:
        d1 += 1
    elif diff == 3:
        d3 += 1
print(f"part 1: {d1 * d3}")

@memoize
def get_next(currentIndex):
    if currentIndex+1 == len(inputs):
        return 1
    validIndexes = set()
    current = inputs[currentIndex]
    for i in range(currentIndex+1, len(inputs)):
        if inputs[i] <= current + 3:
            validIndexes.add(i)
        else:
            break
    return validIndexes

@memoize
def search(index):    
    valid_indexes = get_next(index)
    if valid_indexes == 1:
        return 1
    s = 0
    for index in valid_indexes:
        s += search(index)
    return s

inputs = [0] + inputs

part2 = search(0)
print(f"part 2: {part2}")