inputs = [i for i in open("inputs/day02.txt", 'r').readlines()]

loss_2 = {
    "A": "Z",
    "B": "X",
    "C": "Y",
}
win_2 = {
    "A": "Y",
    "B": "Z",
    "C": "X",
}
tie_2 = {
    "A": "X",
    "B": "Y",
    "C": "Z",
}


scz = {
    "X": 1,
    "Y": 2,
    "Z": 3,
}

loss_pairs = [("A", "Z"), ("B", "X"), ("C", "Y")]
win_pairs = [("A", "Y"), ("B", "Z"), ("C", "X")]


def eval_round(a, b):
    if (a, b) in loss_pairs:
        return scz[b]
    elif (a, b) in win_pairs:
        return scz[b] + 6
    else:
        return scz[b] + 3
    assert False


def eval_round_p2(a, b):
    choice = ""
    score = 0
    if b == "X":
        choice = loss_2[a]
    elif b == "Y":
        choice = tie_2[a]
        score += 3
    elif b == "Z":
        choice = win_2[a]
        score += 6
    score += scz[choice]
    return score


score = 0
for i in inputs:
    a, b = i.strip().split(" ")
    score += eval_round(a, b)
print(f"part 1: {score}")

score = 0
for i in inputs:
    a, b = i.strip().split(" ")
    score += eval_round_p2(a, b)
print(f"part 2: {score}")
