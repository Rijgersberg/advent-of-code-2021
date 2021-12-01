from aoc import get_input


depths = [int(x) for x in get_input(day=1)]

# 1-1
print(sum(next_ > prev for next_, prev in zip(depths[1:], depths[:-1])))


# 1-2
total = 0
prev = float('inf')
for i in range(len(depths) - 2):
    nxt = depths[i+2] + depths[i+1] + depths[i]
    if nxt > prev:
        total += 1
    prev = nxt
print(total)
