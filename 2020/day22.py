input_raw = open("inputs/day22.txt", 'r').read()

decks_raw = input_raw.split("\n\n")

def get_deck_from_raw(lines_raw):
    cards = []
    for card in lines_raw.splitlines()[1:]:
        cards.append(int(card.strip()))
    return cards

pl1_deck = get_deck_from_raw(decks_raw[0])
pl2_deck = get_deck_from_raw(decks_raw[1])

def simulate_game(pl1_deck, pl2_deck):
    pl1_deck, pl2_deck = pl1_deck.copy(), pl2_deck.copy()
    while len(pl1_deck) != 0 and len(pl2_deck) != 0:
        a, b = pl1_deck.pop(0), pl2_deck.pop(0)
        if a > b:
            pl1_deck.append(a)
            pl1_deck.append(b)
        if a < b:
            pl2_deck.append(b)
            pl2_deck.append(a)
    return pl1_deck, pl2_deck

def get_deck_score(deck):
    score = 0
    decklen = len(deck)
    for k, v in enumerate(deck):
        score += v * (decklen - k)
    return score

a, b = simulate_game(pl1_deck, pl2_deck)
winner = {0: b}.get(len(a), a)

part1 = get_deck_score(winner)
print(f"part 1: {part1}")

PLAYERA, PLAYERB, STILL_PLAYING = "player_a", "player_b", "still_playing"

def play_game(hand_a, hand_b):
    prev_rounds = set()

    def play_round(hand_a, hand_b):
        frozen_round = (tuple(hand_a), tuple(hand_b))
        if frozen_round in prev_rounds:
            return PLAYERA
        prev_rounds.add(frozen_round)
        
        a, b = hand_a.pop(0), hand_b.pop(0)

        round_winner = STILL_PLAYING

        if len(hand_a) >= a and len(hand_b) >= b:
            round_winner = play_game(hand_a[:a].copy(), hand_b[:b].copy())
        else:
            if a > b:
                round_winner = PLAYERA
            if b > a:
                round_winner = PLAYERB
        
        if round_winner == PLAYERA:
            hand_a.append(a)
            hand_a.append(b)
        if round_winner == PLAYERB:
            hand_b.append(b)
            hand_b.append(a)
        
        if len(hand_a) == 0:
            return PLAYERB
        if len(hand_b) == 0:
            return PLAYERA
        
        return STILL_PLAYING
    
    while (winner := play_round(hand_a, hand_b)) == STILL_PLAYING: pass

    return winner

game_decks = [deck.copy() for deck in [pl1_deck, pl2_deck]]
winner = play_game(*game_decks)

winner = {
    PLAYERA: game_decks[0],
    PLAYERB: game_decks[1]
}[winner]

part2 = get_deck_score(winner)
print(f"part 2: {part2}")