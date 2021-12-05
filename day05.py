from collections import Counter

from aoc import get_input


def sign(n):
    return n // abs(n)


def play(lines, count_diagonal=False):
    counter = Counter()
    for line in lines:
        start, end = line.split(' -> ')
        start = [int(x) for x in start.split(',')]
        end = [int(x) for x in end.split(',')]

        x_min = min(start[0], end[0])
        x_max = max(start[0], end[0])

        y_min = min(start[1], end[1])
        y_max = max(start[1], end[1])

        if start[0] == end[0]:  # vertical
            x = start[0]
            for y in range(y_min, y_max + 1):
                counter.update([(x, y)])
        elif start[1] == end[1]:  # horizontal
            y = start[1]
            for x in range(x_min, x_max + 1):
                counter.update([(x, y)])
        elif count_diagonal:  # diagonal (45 degrees only, by the description)
            sign_x = sign(end[0] - start[0])
            sign_y = sign(end[1] - start[1])

            xs = list(range(start[0], end[0]+sign_x, sign_x))
            ys = list(range(start[1], end[1]+sign_y, sign_y))
            assert len(xs) == len(ys)

            for (x, y) in zip(xs, ys):
                counter.update([(x, y)])
        else:
            pass
    return counter


print(sum(c >= 2 for c in play(get_input(day=5)).values()))
print(sum(c >= 2 for c in play(get_input(day=5), count_diagonal=True).values()))
