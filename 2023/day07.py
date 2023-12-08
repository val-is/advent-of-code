lines = [i.strip() for i in open('inputs/day07.txt', 'r').readlines()]

hands = []
for line in lines:
    cards, bid = line.split(" ")
    hands.append((cards, int(bid)))

hand_types = {}

def get_rank(hand):
    best_rank = 0
    for sub in "A23456789TQK":
        test_hand = hand.replace("J", sub)
        best_rank =max(best_rank, get_rank_p1(test_hand))
    return best_rank

def get_rank_p1(hand):
    cards = {}
    for card in hand:
        if card in cards:
            cards[card]+= 1
        else:
            cards[card] = 1
    if len(cards) == 1:
        return 7
    if len(cards) == 2:
        max_ = 0
        for k in cards:
            max_ = max(max_, cards[k])
        if max_ == 4:
            return 6
        else:
            return 5
    if len(cards) == 3:
        max_ = 0
        for k in cards:
            max_ = max(max_, cards[k])
        if max_ == 3:
            return 4
        else:
            return 3
    if len(cards) == 4:
        return 2
    if len(cards) == 5:
        return 1
        
part1 = 0
for hand in hands:
    rank = get_rank(hand[0])
    if rank in hand_types:
        hand_types[rank].append(hand)
    else:
        hand_types[rank] = [hand]

sorting_by = {
    'J': 0,
    '2': 1,
    '3': 2,
    '4': 3,
    '5': 4,
    '6': 5,
    '7': 6,
    '8': 7,
    '9': 8,
    'T': 9,
    'Q': 10,
    'K': 11,
    'A': 12
}

def score_hand_tie(hand):
    s = 0
    x = 1
    for h in hand[::-1]:
        s+=sorting_by[h]*x
        x*=len(sorting_by)
    return s

print(score_hand_tie("T55J5"))
print(score_hand_tie("QQQJA"))

for hand in hand_types:
    hand_types[hand] = sorted(hand_types[hand], key=lambda x: score_hand_tie(x[0]))

part1 = 0
acc = 1
for t in [1,2,3,4,5,6,7]:
    if t not in hand_types:
        continue
    for h in hand_types[t]:
        print(h, acc)
        part1 += h[1] * acc
        acc += 1

part2 = 0

print(f"part 1:")
print(f"{part1}")

print(f"part 2:")
print(f"{part2}")