import re

from matplotlib import pyplot as plt
import numpy as np

from aoc import get_input


def parse(lines):
    dot_lines, fold_lines = lines.split('\n\n')

    dots = []
    for line in dot_lines.splitlines():
        x, y = line.split(',')
        dots.append((int(x), int(y)))

    sheet = np.full((max(d[0] for d in dots)+1, max(d[1] for d in dots)+1), False)
    print(sheet.shape)
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
    if direc == 'x':
        empty_sheet = np.full((2*l + 1, sheet.shape[1]), False)
        empty_sheet[:sheet.shape[0], :sheet.shape[1]] = sheet
        sheet = empty_sheet

        left, right = sheet[:l, :], sheet[l+1:, :]
        sheet = left + np.flip(right, axis=0)
    else:
        empty_sheet = np.full((sheet.shape[0], 2*l + 1), False)
        empty_sheet[:sheet.shape[0], :sheet.shape[1]] = sheet
        sheet = empty_sheet

        up, down = sheet[:, :l], sheet[:, l+1:]
        sheet = up + np.flip(down, axis=1)
    if i == 0:
        print(sheet.sum())

plt.imshow(sheet.T)
plt.show()
