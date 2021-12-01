from aoc import get_input


depths = [int(x) for x in get_input(day=1)]

# 1-1
total = 0
for i in range(len(depths) - 1):
    if depths[i+1] > depths[i]:
        total += 1
print(total)


# 1-2
total = 0
prev = float('inf')
for i in range(len(depths) - 2):
    nxt = depths[i+2] + depths[i+1] + depths[i]
    if nxt > prev:
        total += 1
    prev = nxt
print(total)
