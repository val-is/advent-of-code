inputs = [i for i in open('inputs/day2.txt').readlines()]

part1 = 0
for pwrule in inputs:
    # scuffed parsing is scuffed
    quantityraw, char, string = pwrule.split(' ')
    minV, maxV = [int(i) for i in quantityraw.split('-')]
    char = char[0]

    instances = 0
    for i in string:
        if i == char:
            instances += 1
    
    if minV <= instances <= maxV:
        part1 += 1

print(f"part 1: {part1}")

part2 = 0
for pwrule in inputs:
    quantityraw, char, string = pwrule.split(' ')
    minV, maxV = [int(i) for i in quantityraw.split('-')]
    char = char[0]

    if (string[minV-1] == char) ^ (string[maxV-1] == char):
        part2 += 1
        
print(f"part 2: {part2}")
