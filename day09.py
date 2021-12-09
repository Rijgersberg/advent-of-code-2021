from math import prod

from aoc import get_input


heights = [[int(h) for h in row] for row in get_input(day=9)]
R = len(heights)
C = len(heights[0])

def neighbors(r, c):
    for a, b in (r+1, c), (r-1, c), (r, c+1), (r, c-1):
        if 0 <= a < R and 0 <= b < C:
            yield a, b

def calc_low_points(heights):
    low_points = []
    for r, row in enumerate(heights):
        for c, h in enumerate(row):
            if all(h < heights[r_n][c_n] for r_n, c_n in neighbors(r, c)):
                low_points.append((r, c))
    return low_points


# 9-1
low_points = calc_low_points(heights)
print(sum(1 + heights[r][c] for r, c in low_points))

# 9-2
visited = set()
def size(r, c):
    visited.add((r, c))
    return 1 + sum(size(r_n, c_n) for r_n, c_n in neighbors(r, c)
                   if (r_n, c_n) not in visited and heights[r_n][c_n] < 9)


basins = [size(r, c) for r, c in low_points if (r, c) not in visited]
print(prod(sorted(basins, reverse=True)[:3]))