from toolbox import memoize_the_world

inputs = open('inputs/day19.txt', 'r').read().strip()
rules, messages = inputs.split("\n\n")

rules = [i.strip() for i in rules.split("\n")]
messages = [i.strip() for i in messages.split("\n")]

rulesParsed = {}
for rule in rules:
    ruleNum, rest = rule.split(": ", 1)
    ruleNum = int(ruleNum)
    val = None
    if rest.startswith("\""):
        val = rest[1]
    else:
        if "|" in rest:
            p1, p2 = rest.split(" | ")
            p1Parts = p1.split(" ")
            p2Parts = p2.split(" ")
            val = [[int(i) for i in p1Parts], [int(j) for j in p2Parts]]
        else:
            p1 = rest
            p1Parts = p1.split(" ")
            val = [[int(i) for i in p1Parts]]
    rulesParsed[ruleNum] = val

@memoize_the_world
def validate(strIn, ruleNum):
    if strIn == "":
        return False
    
    rule = rulesParsed[ruleNum]
    if rule in ["a", "b"]:
        return strIn == rule
    
    for ruleSet in rule:
        if len(ruleSet) == 1:
            if validate(strIn, ruleSet[0]):
                return True
        if len(ruleSet) == 2:
            for split in range(1, len(strIn)):
                a, b = strIn[:split], strIn[split:]
                if validate(a, ruleSet[0]) and validate(b, ruleSet[1]):
                    return True
        if len(ruleSet) == 3:
            # special case :\
            # there's only one of these
            for splitA in range(1, len(strIn)):
                for splitB in range(splitA, len(strIn)):
                    a, b, c = strIn[:splitA], strIn[splitA:splitB], strIn[splitB:]
                    if a == "" or b == "" or c == "":
                        continue
                    if (validate(a, ruleSet[0]) and 
                        validate(b, ruleSet[1]) and
                        validate(c, ruleSet[2])):
                        return True
    return False

part1 = len([i for i in messages if validate(i, 0)])
print(f"part 1: {part1}")

validate.reset()

rulesParsed[8] = [[42], [42, 8]]
rulesParsed[11] = [[42, 31], [42, 11, 31]]

part2 = len([i for i in messages if validate(i, 0)])
print(f"part 2: {part2}")