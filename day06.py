from collections import Counter, defaultdict

from aoc import get_input


def play(line, T):
    fish = Counter(int(x) for x in line.split(','))
    for t in range(1, T+1):
        next_fish = defaultdict(int)
        for timer, n in fish.items():
            if timer == 0:
                next_fish[8] += n
                next_fish[6] += n
            else:
                next_fish[timer-1] += n
        fish = next_fish
    return sum(fish.values())


# 6-1
assert play('3,4,3,1,2', T=80) == 5934
print(play(get_input(day=6, as_list=False), T=80))

# 6-2
assert play('3,4,3,1,2', T=256) == 26984457539
print(play(get_input(day=6, as_list=False), T=256))
