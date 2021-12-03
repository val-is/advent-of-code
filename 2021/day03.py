inputs = [i.strip() for i in open('inputs/day03.txt', 'r').readlines()]

def filter_by_bit(inputs, position, val):
    return [i for i in inputs if i[position] == val]

def freq_at_pos_val(inputs, position, val):
    return len(filter_by_bit(inputs, position, val))

def freqs_at_pos(inputs, position):
    return {
            '0': freq_at_pos_val(inputs, position, '0'),
            '1': freq_at_pos_val(inputs, position, '1'),
            }

# part 1
gamma = ''
epsilon = ''
for bit in range(len(inputs[0])):
    fs = freqs_at_pos(inputs, bit)
    if fs['0'] > fs['1']:
        gamma += '0'
        epsilon += '1'
    else:
        gamma += '1'
        epsilon += '0'
part1 = int(gamma,2) * int(epsilon,2)
print(f"part 1: {part1}")

# part 2
def filter_by_bit_preserve(inputs, position, val):
    new_inputs = filter_by_bit(inputs, position, val)
    if len(new_inputs) == 0:
        return inputs
    return new_inputs

def filter_by_freqs(inputs, position, inv_selection):
    fs = freqs_at_pos(inputs, position)
    if fs['0'] > fs['1']:
        return filter_by_bit_preserve(inputs, position,
                '0' if not inv_selection else '1')
    else:
        return filter_by_bit_preserve(inputs, position,
                '1' if not inv_selection else '0')


valid_oxy = [i for i in inputs]
valid_co2 = [i for i in inputs]

for bit in range(len(inputs[0])):
    valid_oxy = filter_by_freqs(valid_oxy, bit, False)
    valid_co2 = filter_by_freqs(valid_co2, bit, True)

part2 = int(valid_oxy[0],2) * int(valid_co2[0],2)
print(f"part 2: {part2}")
