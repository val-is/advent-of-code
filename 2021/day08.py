inputs = [i.split(" | ") for i in open('inputs/day08.txt', 'r').readlines()]

def parse_input(i):
    types, digits = i
    types = types.split()
    digits = digits.split()

    identified_nums = []
    for i in digits:
        if len(i) == 2:
            identified_nums.append(1)
        if len(i) == 4:
            identified_nums.append(4)
        if len(i) == 3:
            identified_nums.append(7)
        if len(i) == 7:
            identified_nums.append(8)
    return identified_nums

s = 0
for i in inputs:
    s += len(parse_input(i))

part1 = s
print(f"part 1: {part1}")

def p2_iter(given):
    types, digits = given
    types = types.split()

    types = [{*i} for i in types]

    # pass 1: identify 1, 4, and 7
    one_raw =   [i for i in types if len(i) == 2][0]
    four_raw =  [i for i in types if len(i) == 4][0]
    seven_raw = [i for i in types if len(i) == 3][0]
    eight_raw = [i for i in types if len(i) == 7][0]

    # pass 2: identify 3 using 1
    five_long = [i for i in types if len(i) == 5]
    three_raw = [i for i in five_long if len(i & one_raw) == 2][0]

    # pass 3: split out center 3 pieces
    right_parts = one_raw
    center_parts = three_raw - one_raw

    # pass 4: find top left (b) using 4
    b_char = four_raw - center_parts- right_parts

    # pass 5: find five using knowledge of center and b
    five_raw = [i for i in types if len(i) == 5
                                    and len(i & center_parts) == 3
                                    and len(i & b_char) == 1][0]

    # pass 6: using five, find (f)
    f_char = five_raw & right_parts

    # pass 7: using one, find (c)
    c_char = one_raw - f_char

    # pass 8: using seven, find a
    a_char = seven_raw - f_char - c_char

    # pass 9: using four, find d
    d_char = four_raw - b_char - c_char - f_char

    # pass 10: using 3, find g
    g_char = three_raw - one_raw - a_char - d_char

    # pass 11: using 8, find e
    e_char = eight_raw - a_char - b_char - c_char - d_char - f_char - g_char

    # create translation map
    trans = {
            [*a_char][0]: 'a',
            [*b_char][0]: 'b',
            [*c_char][0]: 'c',
            [*d_char][0]: 'd',
            [*e_char][0]: 'e',
            [*f_char][0]: 'f',
            [*g_char][0]: 'g',
            }

    # translate digits
    s = 0
    for digit in digits.split():
        illuminated = set()
        for char in digit:
            illuminated |= {trans[char]}
        illuminated_str = "".join(sorted(list(illuminated)))
        value = {
                "abcefg": 0,
                "cf": 1,
                "acdeg": 2,
                "acdfg": 3,
                "bcdf": 4,
                "abdfg": 5,
                "abdefg": 6,
                "acf": 7,
                "abcdefg": 8,
                "abcdfg": 9,
                }
        s *= 10
        s += value[illuminated_str]
    return s

s = 0
for i in inputs:
    s += p2_iter(i)

part2 = s
print(f"part 2: {part2}")
