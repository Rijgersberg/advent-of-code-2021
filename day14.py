from collections import Counter
from dataclasses import dataclass
from typing import Optional

from tqdm import tqdm

from aoc import get_input

@dataclass
class Chemical:
    element: str
    next: Optional['Chemical']

polymer, rule_lines = get_input(day=14, as_list=False).split('\n\n')
# polymer, rule_lines = '''NNCB
#
# CH -> B
# HH -> N
# CB -> H
# NH -> C
# HB -> C
# HC -> B
# HN -> C
# NN -> C
# BH -> H
# NC -> B
# NB -> B
# BN -> B
# BB -> N
# BC -> B
# CC -> N
# CN -> C'''.split('\n\n')

next_ = Chemical(polymer[-1], None)
for i in range(len(polymer)-1, 0, -1):
    prev = Chemical(polymer[i-1], next_)
    next_ = prev

rules = {}
for rule in rule_lines.splitlines():
    key, value = rule.split(' -> ')
    rules[key] = value

def show(prev):
    chars = []
    while prev.next is not None:
        chars.append(prev.element)
        prev = prev.next
    chars.append(prev.element)
    print(''.join(chars))


def score(start):
    prev = start
    counter = Counter()
    while prev.next is not None:
        counter.update([prev.element])
        prev = prev.next

    counter.update([prev.element])
    counts = counter.most_common()
    print(counts[0][1])
    return counts[0][1] - counts[-1][1]

start = prev
for t in tqdm(range(1, 40+1)):
    prev = start

    # show(prev)

    while prev.next is not None:
        next = prev.next
        if (key := prev.element + next.element) in rules:
            insert = Chemical(rules[key], next)
            prev.next = insert
        prev = next
    score(start)