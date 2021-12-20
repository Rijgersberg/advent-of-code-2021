from collections import defaultdict

from aoc import get_input


def parse(input_):
    algorithm = [int(c == '#') for c in input_[0]]

    image = defaultdict(int)
    for r, line in enumerate(input_[2:]):
        for c, char in enumerate(line):
            if char == '#':
                image[(r, c)] = 1
    return algorithm, image


def neighbors(r, c):
    for i in (-1, 0, 1):
        for j in (-1, 0, 1):
            yield r+i, c+j


def step(image, algorithm, default):
    new_image = defaultdict(lambda: default)

    rs, cs = zip(*image.keys())
    r_min, r_max = min(rs), max(rs)
    c_min, c_max = min(cs), max(cs)

    for r in range(r_min-1, r_max+1 +1):
        for c in range(c_min-1, c_max+1 +1):
            new_image[(r, c)] = algorithm[int(''.join(str(image[p]) for p in neighbors(r, c)), 2)]

    return new_image

algorithm, image = parse(get_input(day=20))

for t in range(50):
    new_default = algorithm[0] if t % 2 == 0 else 0
    image = step(image, algorithm, new_default)

    if t == 1:
        print(sum(image.values()))
print(sum(image.values()))
