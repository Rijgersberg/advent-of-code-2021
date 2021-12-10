from collections import deque

from aoc import get_input

score_table = {')': 3,
               ']': 57,
               '}': 1197,
               '>': 25137}
opening = '([{<'
closing = ')]}>'

def corrupted(line):
    to_close = deque()
    for i, c in enumerate(line):
        if c in opening:
            to_close.appendleft(c)
        elif c in closing and closing.index(c) == opening.index(to_close[0]):
            _ = to_close.popleft()
        else:
            return i, c, to_close
    return None, None, to_close


lines = get_input(day=10)
score1 = 0
scores2 = []
for line in lines:
    pos, missing, to_close = corrupted(line)
    if missing is not None:
        score1 += score_table[missing]
    else:
        score2 = 0
        for c in to_close:
            score2 = score2 * 5 + 1 + opening.index(c)
        scores2.append(score2)
print(score1)
print(sorted(scores2)[len(scores2)//2])
