inputs = open('inputs/day19.txt', 'r').read()

scanners = []
for scanner in inputs.split("\n\n"):
    beacons = set()
    for line in scanner.strip().split("\n")[1:]:
        a, b, c = [int(i) for i in line.strip().split(",")]
        beacons.add((a,b,c))
    scanners.append(beacons)

def get_perms(coord):
    a, b, c = coord
    return [
            (a,b,c),
            (a,-b,-c),
            (-a,b,-c),
            (-a,-b,c),
            
            (-a,-c,-b),
            (-a,c,b),
            (a,-c,b),
            (a,c,-b),
            
            (b,c,a),
            (b,-c,-a),
            (-b,c,-a),
            (-b,-c,a),
            
            (-b,-a,-c),
            (-b,a,c),
            (b,-a,c),
            (b,a,-c),
            
            (c,a,b),
            (c,-a,-b),
            (-c,a,-b),
            (-c,-a,b),
            
            (-c,-b,-a),
            (-c,b,a),
            (c,-b,a),
            (c,b,-a),
            ]

def get_permutes_scan(beacon):
    return [*zip(*[get_perms(i) for i in beacon])]

def apply_offset(beacons, offset):
    return {
            (b[0]+offset[0], b[1]+offset[1], b[2]+offset[2]) for b in beacons
            }

fixed_beacons = scanners[0]
fixed_scanners = [scanners[0]]
offsets = [(0,0,0)]

scanners = scanners[1:]

def inner(fixed_beacons, fixed_scanners, offsets):
    for k, v in enumerate(scanners):
        for perm in get_permutes_scan(v):
            for base_beak in fixed_beacons:
                for blip in perm:
                    offset = (base_beak[0]-blip[0], base_beak[1]-blip[1], base_beak[2]-blip[2])
                    testing = apply_offset(perm, offset)
                    aligned = testing & fixed_beacons
                    if len(aligned) >= 12:
                        fixed_beacons = fixed_beacons | testing
                        fixed_scanners.append(testing)
                        offsets.append(offset)
                        return k, fixed_beacons, fixed_scanners, offsets
    return None

while len(scanners) > 1:
    rem, fixed_beacons, fixed_scanners, offsets = inner(fixed_beacons, fixed_scanners, offsets)
    if rem != None: 
        scanners.pop(rem)

print("p1: ", len(fixed_beacons))

max_offset_dist = 0
for k, i in enumerate(offsets):
    for k2, j in enumerate(offsets):
        if k == k2:
            continue
        dist = sum([abs(j[n]-i[n]) for n in range(3)])
        max_offset_dist = max(max_offset_dist, dist)
print("p2: ", max_offset_dist)
