inputs = open("inputs/day06.txt", 'r').read().strip()

def find_marker(inputs, seq_len):
    prev_building = ""
    for k, i in enumerate(inputs):
        prev_building = prev_building + i
        if len(prev_building) > seq_len:
            prev_building = prev_building[1:seq_len+1]
        if len(set([i for i in prev_building])) == seq_len:
            return k + 1

part_1 = find_marker(inputs, 4)
print(f"part 1: {part_1}")

part_2 = find_marker(inputs, 14)
print(f"part 2: {part_2}")
