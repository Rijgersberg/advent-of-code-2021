from collections import defaultdict
from itertools import pairwise
from operator import itemgetter

from aoc import get_input


polymer, rule_lines = get_input(day=14, as_list=False).split('\n\n')

pairs = defaultdict(int)
for a, b in pairwise(polymer):
    pairs[a+b] += 1

rules = {}
for rule in rule_lines.splitlines():
    key, value = rule.split(' -> ')
    rules[key] = value


def count_single_letters(pairs):
    counts = defaultdict(int)
    for pair, count in pairs.items():
        a, b = pair
        counts[a] += count / 2
        counts[b] += count / 2
    counts[polymer[0]] += 0.5
    counts[polymer[-1]] += 0.5
    return {k: int(v) for k, v in counts.items()}


for t in range(1, 40+1):
    new_pairs = defaultdict(int)
    for pair, count in pairs.items():
        if pair in rules:
            a, b = pair
            inserted = rules[pair]
            new_pairs[a+inserted] += count
            new_pairs[inserted+b] += count
        else:
            new_pairs[pair] += count
    pairs = new_pairs

    if t == 10 or t == 40:
        letter_counts = [v for k, v in sorted(count_single_letters(pairs).items(),
                                              key=itemgetter(1),
                                              reverse=True)]
        print(letter_counts[0] - letter_counts[-1])
