import math

def swap(numbers, from_idx, to_idx):
    f = None
    t = None
    print(from_idx, to_idx)
    from_idx %= len(numbers)
    to_idx %= len(numbers)
    print(from_idx, to_idx)
    for i in numbers:
        if numbers[i][0] == from_idx:
            f = i
        if numbers[i][0] == to_idx:
            t = i
        if f != None and t != None:
            break
    numbers[f], numbers[t] = (numbers[t][0], numbers[f][1]), (numbers[f][0], numbers[t][1])
    return numbers

def print_arr(arr):
    for idx in range(len(arr)):
        for a in arr:
            if arr[a][0] == idx:
                print(arr[a][1], end=", ")
    print()

def run(fname):
    lines = [i.strip() for i in open(fname, 'r').readlines()]
    ints = [*map(int, lines)]
    initial_config = {k: (k, v) for k, v in enumerate(ints)} # original_pos : (cur_pos, val)
    for i in range(len(ints)):
        swaps = initial_config[i][1]
        if swaps == 0:
            continue
        else:
            initial_config = swap(initial_config, initial_config[i][0], initial_config[i][0]+swaps)
        print_arr(initial_config)
    
    part1 = 0
    part2 = 0

    print(f"part 1:")
    print(f"{part1}")

    print(f"part 2:")
    print(f"{part2}")

print("TEST")
run('inputs/test.txt')
# print()
# print("REAL")
# run('inputs/day20.txt')