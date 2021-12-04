from copy import deepcopy

from aoc import get_input


class BingoCard:
    def __init__(self, board):
        self.board = [[int(n) for n in line.split()]
         for line in board.split('\n')]

        self.marked = [[False for _ in line] for line in self.board]

    def add(self, number):
        for r, row in enumerate(self.board):
            for c, n in enumerate(row):
                if n == number:
                    self.marked[r][c] = True

    def bingo(self):
        for row in self.marked:
            if all(row):
                return True

        for col in zip(*self.marked):
            if all(col):
                return True

        return False

    def score(self):
        s = 0
        for r, row in enumerate(self.board):
            for c, n in enumerate(row):
                if not self.marked[r][c]:
                    s += n
        return s


def parse(puzzle):
    bingo_numbers, boards = puzzle.split('\n\n', 1)

    bingo_numbers = [int(n) for n in bingo_numbers.split(',')]
    boards = [BingoCard(board) for board in boards.split('\n\n')]

    return bingo_numbers, boards


bingo_numbers, boards = parse(get_input(day=4, as_list=False))

# 4-1
def play(bingo_numbers, boards):
    for number in bingo_numbers:
        for board in boards:
            board.add(number)
            if board.bingo():
                return number * board.score()
print(play(bingo_numbers, deepcopy(boards)))


# 4-2
def play2(bingo_numbers, boards):
    not_won_yet = set(range(len(boards)))

    for number in bingo_numbers:
        for i, board in enumerate(boards):
            board.add(number)
            if board.bingo():
                not_won_yet -= {i}
            if not_won_yet == set():
                return number * board.score()
print(play2(bingo_numbers, deepcopy(boards)))
