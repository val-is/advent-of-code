import re


data = open('inputs/day4.txt', 'r').read().strip()
portsRaw = data.split('\n\n')

types = [
            "byr",
            "iyr",
            "eyr",
            "hgt",
            "hcl",
            "ecl",
            "pid",
            "cid"
        ]

ports = []
for i in portsRaw:
    fields = re.split(r'\n| ', i)
    struct = {}
    for f in fields:
        for t in types:
            if f.startswith(t):
                struct[t] = f[4:]
    ports += [struct]

def checkValidp1(port):
    for t in types:
        if t not in port.keys() and t != "cid":
            return False
    return True

vports = []
for port in ports:
    if checkValidp1(port):
        vports += [port]
print(f"part 1: {len(vports)}")

def getYear(yStr):
    if not yStr.isnumeric():
        return 0, False
    return int(yStr), True

def getValidHgt(hgtStr):
    intPart = hgtStr[:-2]
    units = hgtStr[-2:]
    if not intPart.isnumeric():
        return False
    hgt = int(intPart)
    if units == "cm":
        if not( 150 <= hgt <= 193):
            return False
    if units == "in":
        if not (59 <= hgt <= 76):
            return False
    if units not in ["cm", "in"]:
        return False
    return True

def checkHair(clr):
    if len(clr) != 7 or clr[0] != "#":
        return False
    if not re.match(r"#[0-9a-f]{6}", clr):
        return False
    return True

def checkEye(eyeclr):
    if eyeclr not in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
        return False
    return True

def checkPid(pid):
    if not pid.isnumeric():
        return False
    if len(pid) != 9 or pid[0] == "-":
        return False
    return True

def checkValidp2(port):    
    yr, valid = getYear(port["byr"])
    if not valid:
        return False
    if yr < 1920 or yr > 2002:
        return False
    
    yr, valid = getYear(port["iyr"])
    if not valid:
        return False
    if yr < 2010 or yr > 2020:
        return False

    yr, valid = getYear(port["eyr"])
    if not valid:
        return False
    if yr < 2020 or yr > 2030:
        return False

    if not getValidHgt(port["hgt"]):
        return False
    
    if not checkEye(port["ecl"]):
        return False
    
    if not checkHair(port["hcl"]):
        return False

    if not checkPid(port["pid"]):
        return False

    return True

part2 = 0
for port in vports:
    if checkValidp2(port):
        part2 += 1
print(f"part 2: {part2}")