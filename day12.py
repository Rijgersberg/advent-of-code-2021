from collections import defaultdict

from aoc import get_input


def parse(lines):
    edgelist = defaultdict(list)
    for line in lines:
        a, b = line.split('-')
        edgelist[a].append(b)
        edgelist[b].append(a)
    return edgelist


def rule1(path, nxt):
    return not (nxt.islower() and nxt in path[:-1])


def rule2(path, nxt):
    if nxt.isupper() or nxt not in path:
        return True

    lower = [node for node in path if node.islower()]
    return len(lower) == len(set(lower))  # no lowercaves visited more than once


def find(target, path, rule):
    current = path[-1]

    if current == target:
        return {path}

    found_paths = set()
    for nxt in edgelist[current]:
        if nxt != 'start' and rule(path, nxt):
            found_paths |= find(target, path + (nxt,), rule)
    return found_paths


edgelist = parse(get_input(day=12))
print(len(find('end', ('start', ), rule=rule1)))
print(len(find('end', ('start', ), rule=rule2)))
