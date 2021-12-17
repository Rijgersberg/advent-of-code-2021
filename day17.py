target = set()
for x in range(206, 250+1):
    for y in range(-105, -57+1):
        target.add((x, y))


def shoot(v_x, v_y, target, max_x, min_y):
    x, y = 0, 0

    max_y = y
    while x <= max_x and y >= min_y:
        x += v_x
        y += v_y
        v_x = max(0, v_x - 1)
        v_y -= 1

        if y > max_y:
            max_y = y

        if (x, y) in target:
            return True, max_y
    return False, max_y


max_x = max(t[0] for t in target)
min_y = min(t[1] for t in target)

max_y = -1e9
n_hits = 0
for v_x in range(max_x+1):
    for v_y in range(min_y, 300):
        hit, y_reached = shoot(v_x, v_y, target, max_x, min_y)
        if hit:
            n_hits += 1
            max_y = max(max_y, y_reached)
print(max_y, n_hits)
