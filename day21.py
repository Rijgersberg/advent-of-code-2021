from functools import cache
from itertools import cycle

from more_itertools import chunked


def deterministic_dice(low, high, chunk_size):
    return chunked(cycle(range(low, high+1)), chunk_size)


def play(pos, winning_score):
    dice = deterministic_dice(1, 100, 3)

    die_rolls = 0
    score = [0, 0]
    for turn in range(1, 1000):
        for player in range(len(pos)):
            die_rolls += 3
            pos[player] = ((pos[player] + sum(next(dice)) - 1) % 10) + 1
            score[player] += pos[player]

            if score[player] >= winning_score:
                return die_rolls, turn, player, pos, score


die_rolls, turn, winning_player, pos, score = play([8, 7], 1000)
print(score[1 if winning_player == 0 else 0] * die_rolls)


# 21-2
dirac_rolls = {i: 0 for i in range(3, 9+1)}
for d1 in range(1, 3+1):
    for d2 in range(1, 3+1):
        for d3 in range(1, 3+1):
            dirac_rolls[d1+d2+d3] += 1

@cache
def play2(pos_in, scores_in, winning_score, player):
    wins = [0, 0]

    for throw, number in dirac_rolls.items():
        pos, scores = list(pos_in), list(scores_in)

        pos[player] = ((pos[player] + throw - 1) % 10) + 1
        scores[player] += pos[player]

        if scores[player] >= winning_score:
            wins[player] += number
        else:
            wins0, wins1 = play2(tuple(pos), tuple(scores), winning_score, 1 if player == 0 else 0)
            wins[0] += number * wins0
            wins[1] += number * wins1
    return wins


print(max(play2((8, 7), (0, 0), winning_score=21, player=0)))
