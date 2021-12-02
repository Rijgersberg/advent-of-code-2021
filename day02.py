from aoc import get_input


# 2-1
depth = 0
pos = 0
for instruction in get_input(day=2):
    match instruction.split():
        case 'forward', x:
            pos += int(x)
        case 'down', x:
            depth += int(x)
        case 'up', x:
            depth -= int(x)
        case _:
            raise ValueError
print(depth * pos)


# 2-2
depth = 0
pos = 0
aim = 0
for instruction in get_input(day=2):
    match instruction.split():
        case 'forward', x:
            x = int(x)
            pos += x
            depth += aim * x
        case 'down', x:
            aim += int(x)
        case 'up', x:
            aim -= int(x)
        case _:
            raise ValueError
print(depth * pos)
