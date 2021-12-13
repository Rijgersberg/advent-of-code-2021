import re

from matplotlib import pyplot as plt
import numpy as np

from aoc import get_input


def parse(lines):
    dot_lines, fold_lines = lines.split('\n\n')

    dots = [tuple(map(int, line.split(','))) for line in dot_lines.splitlines()]
    X, Y = max(d[0] for d in dots)+1, max(d[1] for d in dots)+1
    sheet = np.full((X, Y), False)
    for x, y in dots:
        sheet[x, y] = True

    pattern = r'fold along ([xy])=(\d+)'
    folds = []
    for line in fold_lines.splitlines():
        direction, l = re.fullmatch(pattern, line).groups()
        folds.append((direction, int(l)))
    return sheet, folds


sheet, folds = parse(get_input(day=13, as_list=False))

for i, (direc, l) in enumerate(folds):
    if direc == 'y':
        sheet = sheet.T

    if 2*l + 1 > sheet.shape[0]:
        empty_sheet = np.full((2*l + 1, sheet.shape[1]), False)
        empty_sheet[:sheet.shape[0], :sheet.shape[1]] = sheet
        sheet = empty_sheet

    left, right = sheet[:l, :], sheet[l+1:, :]
    sheet = left + np.flip(right, axis=0)

    if direc == 'y':
        sheet = sheet.T

    if i == 0:
        print(sheet.sum())

plt.imshow(sheet.T)
plt.show()
