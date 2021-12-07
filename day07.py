from aoc import get_input


def fuel(crabs, target):
    return sum(abs(crab-target) for crab in crabs)


def fuel2(crabs, target):
    return sum(abs(crab-target)*(abs(crab-target)+1)//2 for crab in crabs)


crabs = [int(crab) for crab in get_input(day=7, as_list=False).split(',')]
print(min(fuel(crabs, target) for target in range(min(crabs), max(crabs)+1)))
print(min(fuel2(crabs, target) for target in range(min(crabs), max(crabs)+1)))
