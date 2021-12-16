inputs = open('inputs/day16.txt', 'r').read()

bytes = []
for i in inputs.strip():
    v = int(i, 16)
    bytes += [int(j) for j in bin(v)[2:].zfill(4)]

part1 = 0
pointer = 0

def to_int(arr):
    return int("".join([str(i) for i in arr]), 2)

def parse_packet_version(bytes, pointer):
    ver_sum = to_int(bytes[pointer:pointer+3])
    pointer += 3
    
    packet_type = to_int(bytes[pointer:pointer+3])
    pointer += 3

    if packet_type == 4:
        # literal
        vs = []
        while True:
            vs += bytes[pointer+1:pointer+5]
            if bytes[pointer] == 0:
                pointer += 5
                break
            pointer += 5
        value = to_int(vs)
    else:
        # operator
        lti = bytes[pointer]
        vals = []
        pointer += 1
        if lti == 0:
            bitlen = to_int(bytes[pointer:pointer+15])
            pointer += 15
            target_bytes = bitlen + pointer
            while pointer < target_bytes:
                a, val, b = parse_packet_version(bytes, pointer)
                vals.append(val)
                pointer = b
                ver_sum += a
        else:
            n_subpackets = to_int(bytes[pointer:pointer+11])
            pointer += 11
            for _ in range(n_subpackets):
                a, val, b = parse_packet_version(bytes, pointer)
                pointer = b
                vals.append(val)
                ver_sum += a
        
        if packet_type == 0:
            value = sum(vals)
        elif packet_type == 1:
            value = 1
            for i in vals:
                value *= i
        elif packet_type == 2:
            value = min(vals)
        elif packet_type == 3:
            value = max(vals)
        elif packet_type == 5:
            value = 1 if vals[0] > vals[1] else 0
        elif packet_type == 6:
            value = 1 if vals[0] < vals[1] else 0
        elif packet_type == 7:
            value = 1 if vals[0] == vals[1] else 0

    return ver_sum, value, pointer

part1, part2, _ = parse_packet_version(bytes, 0)

print(f"part 1: {part1}")
print(f"part 2: {part2}")
