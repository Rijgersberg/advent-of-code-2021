from itertools import permutations

from aoc import get_input


"""
  0:      1:      2:      3:      4:
 aaaa    ....    aaaa    aaaa    ....
b    c  .    c  .    c  .    c  b    c
b    c  .    c  .    c  .    c  b    c
 ....    ....    dddd    dddd    dddd
e    f  .    f  e    .  .    f  .    f
e    f  .    f  e    .  .    f  .    f
 gggg    ....    gggg    gggg    ....

  5:      6:      7:      8:      9:
 aaaa    aaaa    aaaa    aaaa    aaaa
b    .  b    .  .    c  b    c  b    c
b    .  b    .  .    c  b    c  b    c
 dddd    dddd    ....    dddd    dddd
.    f  e    f  .    f  e    f  .    f
.    f  e    f  .    f  e    f  .    f
 gggg    gggg    ....    gggg    gggg"""
DIGITS = {frozenset('abcefg'): 0,
          frozenset('cf'): 1,
          frozenset('acdeg'): 2,
          frozenset('acdfg'): 3,
          frozenset('bcdf'): 4,
          frozenset('abdfg'): 5,
          frozenset('abdefg'): 6,
          frozenset('acf'): 7,
          frozenset('abcdefg'): 8,
          frozenset('abcdfg'): 9}

MYSTERY_DIGITS = {letters: digit for letters, digit in DIGITS.items() if digit not in {1, 4, 7, 8}}


def part1(lines):
    total = 0
    for line in lines:
        input_, output = line.split(' | ')
        total += sum(len(digit) in {2, 3, 4, 7} for digit in output.split())
    return total


def brute_force(codes):
    for attempt in permutations('abcdefg'):
        mapping = {k: v for k, v in zip(attempt, 'abcdefg')}

        if all(frozenset(''.join(mapping[c] for c in code)) in DIGITS for code in codes):
            return mapping
    raise ValueError


def part2(lines):
    total = 0
    for line in lines:
        input_, output = line.split(' | ')
        mapping = brute_force(input_.split())

        total += int(''.join(str(DIGITS[frozenset(mapping[c] for c in out)]) for out in output.split()))
    return total


print(get_input(day=8))
print(part1(get_input(day=8)))
print(part2(get_input(day=8)))

