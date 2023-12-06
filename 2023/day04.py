lines = [i.strip() for i in open('inputs/day04.txt', 'r').readlines()]

part1 = 0
part2 = 0

cards = []
winnings = {}

for line in lines:
    ccc, line = line.split(": ")
    card_num = int(ccc.split(" ")[-1].strip())
    have, winning = line.split(" | ")
    have = set(map(int, have.split()))
    winning = set(map(int, winning.split()))
    total =  have & winning
    cards += [card_num]
    if len(total) == 0:
        continue
    winnings[card_num] = total
    part1 += 2**(len(total)-1)

print(f"part 1:")
print(f"{part1}")

won_cards = {}
cards_scratching = {k: 1 for k in cards}
for card_num in sorted([*winnings.keys()]):
    total_won = len(winnings[card_num])
    for i in range(total_won):
        if card_num + i+1 in cards_scratching:
            cards_scratching[card_num + i+1] += cards_scratching[card_num]
for k in cards_scratching:
    part2 += cards_scratching[k]

print(f"part 2:")
print(f"{part2}")