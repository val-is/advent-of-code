inputs = [i.strip() for i in open('inputs/day5.txt', 'r').readlines()]

seatLocs = {}
for ticket in inputs:
    rowInstr = ticket[:7]
    colInstr = ticket[-3:]
    
    minRow = 0
    maxRow = 128
    for i in rowInstr:
        mid = (minRow + maxRow) / 2
        if i == "F":
            maxRow = mid
        if i == "B":
            minRow = mid
    row = minRow

    minCol = 0
    maxCol = 8
    for i in colInstr:
        mid = (minCol + maxCol) / 2
        if i == "L":
            maxCol = mid
        if i == "R":
            minCol = mid
    col = minCol

    seatLocs[ticket] = (row, col)

seatIds = []
part1 = 0
for seat in seatLocs:
    row, col = seatLocs[seat]
    i = 8 * row + col
    seatIds.append(i)
    part1 = max(part1, i)
print(f"part 1: {part1}")

seatIds = sorted(seatIds)

possibleSeats = []
for a in ["F", "B"]:
    for b in ["F", "B"]:
        for c in ["F", "B"]:
            for d in ["F", "B"]:
                for e in ["F", "B"]:
                    for f in ["F", "B"]:
                        for g in ["F", "B"]:
                            for h in ["R", "L"]:
                                for i in ["R", "L"]:
                                    for j in ["R", "L"]:
                                        possibleSeats += [a+b+c+d+e+f+g+h+i+j]

seatCandidates = set()
part2 = 0
for ticket in possibleSeats:
    if ticket not in inputs:
        seatCandidates.add(ticket)

for ticket in seatCandidates:
    rowInstr = ticket[:7]
    colInstr = ticket[-3:]
    
    minRow = 0
    maxRow = 128
    for i in rowInstr:
        mid = (minRow + maxRow) / 2
        if i == "F":
            maxRow = mid
        if i == "B":
            minRow = mid
    row = minRow

    minCol = 0
    maxCol = 8
    for i in colInstr:
        mid = (minCol + maxCol) / 2
        if i == "L":
            maxCol = mid
        if i == "R":
            minCol = mid
    col = minCol

    seatId = 8 * row + col

    for k, v in enumerate(seatIds[:-1]):
        if seatIds[k+1] - v == 2 and v+1 == seatId:
            part2 = seatId

print(f"part 2: {part2}")