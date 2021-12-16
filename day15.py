from heapq import heapify, heappop, heappush

from aoc import get_input


input_ = get_input(day=15)

risks = {}
for r, line in enumerate(input_):
    for c, risk in enumerate(line):
        risks[(r, c)] = int(risk)
R = len(input_)
C = len(input_[0])


def neighbors(r, c):
    for rr, cc in (r+1, c), (r-1, c), (r, c+1), (r, c-1):
        if 0 <= rr < R and 0 <= cc < C:
            yield rr, cc


def dijkstra(risks, start, target):
    unvisited = set(risks.keys())

    distances = {start: 0}
    dist_heap = [(0, start)]
    heapify(dist_heap)

    def lowest_unvisited(dist_heap, unvisited):
        while True:
            current_dist, current = heappop(dist_heap)
            if current in unvisited:
                return current_dist, current

    while target in unvisited:
        current_dist, current = lowest_unvisited(dist_heap, unvisited)

        for n in neighbors(*current):
            if n in unvisited:
                tentative_d = current_dist + risks[n]
                if n not in distances or tentative_d < distances[n]:
                    heappush(dist_heap, (tentative_d, n))
                    distances[n] = tentative_d
        unvisited.remove(current)
    return distances[target]


print(dijkstra(risks, (0, 0), (R-1, C-1)))

risks2 = {}
for j in range(5):
    for i in range(5):
        for (r, c), risk in risks.items():
            new_risk = (risk + i + j)
            risks2[(R*j + r, C*i + c)] = new_risk if new_risk <= 9 else new_risk % 10 + 1
R = 5 * R
C = 5 * C

print(dijkstra(risks2, (0, 0), (R-1, C-1)))
