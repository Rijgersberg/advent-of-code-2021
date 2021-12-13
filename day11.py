from aoc import get_input


octopi = [[int(o) for o in row] for row in get_input(day=11)]
R = len(octopi)
C = len(octopi[0])


def neighbors(r, c):
    for i in (-1, 0, 1):
        for j in (-1, 0, 1):
            rr, cc = r + i, c + j
            if not (i == 0 and j == 0) and 0 <= rr < R and 0 <= cc < C:
                yield rr, cc

def add(octopi, n):
    for r, row in enumerate(octopi):
        for c, o in enumerate(row):
            octopi[r][c] += n
    return octopi

def reset(octopi):
    for r, row in enumerate(octopi):
        for c, o in enumerate(row):
            if o is None:
                octopi[r][c] = 0
    return octopi

def search(octopi, n):
    positions = []
    for r, row in enumerate(octopi):
        for c, o in enumerate(row):
            if o is not None and o > n:
                positions.append((r, c))
    return positions

def flash(octopi):
    flashes = 0
    while positions := search(octopi, 9):
        for r, c in positions:
            octopi[r][c] = None
            flashes += 1
            for rr, cc in neighbors(r, c):
                if octopi[rr][cc] is not None:
                    octopi[rr][cc] += 1
    return octopi, flashes


flashes = 0
for t in range(1, 1_000_000):
    octopi = add(octopi, 1)
    octopi, turn_flashes = flash(octopi)
    flashes += turn_flashes

    if t == 100 + 1:
        print(flashes)
    if all(all(o is None for o in row) for row in octopi):
        print(t)
        break
    octopi = reset(octopi)
