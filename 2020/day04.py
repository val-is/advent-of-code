import re

data = open('inputs/day4.txt', 'r').read().strip()
ports_raw = data.split('\n\n')

field_types = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"]

def parse_port(raw):
    fields = re.split(r'\n| ', raw)
    port = {}
    for f in fields:
        t = f[:3]
        if t not in field_types:
            return port, False
        port[t] = f[4:]
    return port, True

ports = []
for i in ports_raw:
    port, valid = parse_port(i)
    if not valid:
        continue
    ports += [port]

def check_fields_present(port):
    for field in field_types:
        if field not in port.keys() and field != "cid":
            return False
    return True

vports = [port for port in ports if check_fields_present(port)]
print(f"part 1: {len(vports)}")

def check_height(height_raw):
    unit = height_raw[-2:]
    if unit not in ["cm", "in"]:
        return False
    hgt = int(height_raw[:-2])
    return {
        "cm": lambda x: 150 <= x <= 193,
        "in": lambda x: 59 <= x <= 76
    }[unit](hgt)

def validate_fields(port):
    if not check_fields_present(port):
        return False
    for field in port:
        if not {
            "byr": lambda x: 1920 <= int(x) <= 2002,
            "iyr": lambda x: 2010 <= int(x) <= 2020,
            "eyr": lambda x: 2020 <= int(x) <= 2030,
            "hgt": check_height,
            "ecl": lambda x: x in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"],
            "hcl": lambda x: re.match(r"^#[0-9a-f]{6}$", x) != None,
            "pid": lambda x: re.match(r"^\d{9}$", x) != None
        }.get(field, lambda x: True)(port[field]):
            return False
    return True

vports = [port for port in vports if validate_fields(port)]
print(f"part 2: {len(vports)}")