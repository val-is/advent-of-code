data = open('inputs/day5.txt', 'r').readlines()

vowels = 'aeiou'
disallowed = {'ab', 'cd', 'pq', 'xy'}

def eval_string(s):
    for d in disallowed:
        if d in s:
            return False

    v_count = 0
    d_letter = False
    for k, v in enumerate(s):
        if v in vowels:
            v_count += 1
        if k > 0 and s[k-1] == v:
            d_letter = True
    return v_count >= 3 and d_letter

nice_strings = [1 for i in data if eval_string(i)]
print(f"part 1: {len(nice_strings)}")

def eval_string_p2(s):
    pairs = set()
    pair_found = False
    repeater = False
    for k, v in enumerate(s):
        if k > 1 and s[k-2] == v:
            repeater = True
        if k > 0:
            cur_pair = (s[k-1], v)
            if cur_pair in pairs:
                if k > 1 and not (s[k-2] == s[k-1] == v):
                    pair_found = True
            pairs.add(cur_pair)
    return repeater and pair_found

nice_strings = [1 for i in data if eval_string_p2(i)]
print(f"part 2: {len(nice_strings)}")