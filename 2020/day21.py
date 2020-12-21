inputs = [i.strip() for i in open("inputs/day21.txt", 'r').readlines()]

lines = set()
all_ingredients = set()
all_allergens = set()
for line in inputs:
    ing, allerg = line.split("(contains ")
    ingredients = frozenset(ing[:-1].split(" "))
    allergens = frozenset(allerg[:-1].split(", "))
    lines.add((ingredients, allergens))
    for i in ingredients:
        all_ingredients.add(i)
    for a in allergens:
        all_allergens.add(a)

possible = {}
for allergen in all_allergens:
    for recipe in lines:
        ing, aler = recipe
        if allergen in aler:
            if allergen not in possible:
                possible[allergen] = ing.copy()
            else:
                possible[allergen] = possible[allergen].intersection(ing)

known = set()
for val in possible.values():
    for item in val:
        known.add(item)
impossible = all_ingredients - known
acc = 0
for recipe in lines:
    for i in impossible:
        if i in recipe[0]:
            acc += 1

print(f"Part 1: {acc}")

def check_complete():
    for p in possible.values():
        if len(p) != 1:
            return False
    return True

while not check_complete():
    known = set()

    for p in possible:
        if len(possible[p]) == 1:
            known = known.union(possible[p])
    
    for p in possible:
        if len(possible[p]) != 1:
            possible[p] = possible[p] - known

danger = ""
for k in sorted(possible.keys()):
    danger += [*possible[k]][0] + ","
print(f"part 2: {danger[:-1]}")
