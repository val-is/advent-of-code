inputs = [i for i in open('inputs/day7.txt', 'r').readlines()]

bagStruct = {}
import re

bagRe = r"^(.*) bags?$"

def extractBag(i):
    matches = re.match(bagRe, i)
    if matches == None:
        return None
    return matches[1]

for bag in inputs:
    outer = bag.split(" bags contain")[0]
    inner = bag.split(" bags contain ")[1]
    a = {}
    if "no other bags" not in inner:
        for i in inner.strip()[:-1].split(", "):
            count, t = i.split(" ", 1)
            t = extractBag(t)
            if t != None:
                a[t] = int(count)
    else:
        a = {}
    bagStruct[outer] = a


target = "shiny gold"
part1 = 0
def search(root):
    if root == None:
        s = 0
        for bag in bagStruct:
            s += search(bag)
            # print("----")
        return s
    bagContents = bagStruct[root]
    if target in bagContents:
        return 1
    # if target == root:
    #     return 1

    s = 0
    for bag in bagContents:
        s += search(bag)
    # if s != 0:
    #     s = 1
    return s
part1 = search(None)

# part1 = 0
# for bag in bagStruct:
#     if target in bag:
#         part1+=1

print(f"part 1: {part1}")

part2 = 0
def search2(root):
    bagContents = bagStruct[root]
    s = 0
    for bag in bagContents:
        s += (search2(bag) + 1) * bagContents[bag]
    return s
part2 = search2(target)
print(f"part 2: {part2}")