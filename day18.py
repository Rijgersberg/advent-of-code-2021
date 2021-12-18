from copy import deepcopy
from functools import reduce
from itertools import permutations
from math import ceil, floor

from aoc import get_input


def leftmost_pair(example):
    for i, pair in enumerate(example):
        if isinstance(pair, list):
            return i, pair
    return None, None


def first_number_left(example, i):
    for i in range(i-1, 0-1, -1):
        if isinstance(example[i], int):
            return i, example[i]
    return None, 0


def first_number_right(example, i):
    for i in range(i+1, len(example), 1):
        if isinstance(example[i], int):
            return i, example[i]
    return None, 0


def add_left_deepest_int(x, value):
    if isinstance(x, int):
        return False

    if isinstance(x[0], int):
        x[0] += value
        return True
    else:
        return add_left_deepest_int(x[0], value)


def add_right_deepest_int(x, value):
    if isinstance(x, int):
        return False

    if isinstance(x[-1], int):
        x[-1] += value
        return True
    else:
        return add_right_deepest_int(x[-1], value)


def explode(example, level=1):
    if isinstance(example, int):
        return False, example, None, None

    a, b = example
    if level == 4:
        if isinstance(a, list):
            a1, a2 = a
            a = 0

            if isinstance(b, int):
                b = a2 + b
                add_right = None
            else:
                success = add_left_deepest_int(b, a2)
                add_right = None if success else a2

            return True, [a, b], a1, add_right

        elif isinstance(b, list):
            b1, b2 = b
            b = 0

            if isinstance(a, int):
                a = b1 + a
                add_left = None
            else:
                success = add_right_deepest_int(a, b1)
                add_left = None if success else b1
            return True, [a, b], add_left, b2

    exploded_a, a, add_left, add_right = explode(a, level=level+1)
    if add_right is not None:
        if isinstance(b, int):
            b += add_right
            add_right = None
        else:
            success = add_left_deepest_int(b, add_right)
            add_right = None if success else add_right

    exploded_b = False
    if not exploded_a:
        exploded_b, b, add_left, add_right = explode(b, level=level+1)
        if add_left is not None:
            if isinstance(a, int):
                a += add_left
                add_left = None
            else:
                success = add_right_deepest_int(a, add_left)
                add_left = None if success else add_left

    return exploded_a or exploded_b, [a, b], add_left, add_right

assert explode([[[[[9,8],1],2],3],4]) == (True, [[[[0,9],2],3],4], 9, None)
assert explode([7,[6,[5,[4,[3,2]]]]]) == (True, [7,[6,[5,[7,0]]]], None, 2)
assert explode([[6,[5,[4,[3,2]]]],1]) == (True, [[6,[5,[7,0]]],3], None, None)
assert explode([[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]]) == (True, [[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]], None, None)
assert explode([[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]) == (True, [[3,[2,[8,0]]],[9,[5,[7,0]]]], None, 2)


def split(example):
    if isinstance(example, int):
        if example >= 10:
            return True, [floor(example / 2), ceil(example / 2)]
        else:
            return False, example

    a, b = example

    split_a, a = split(a)
    if split_a:
        return True, [a, b]

    split_b, b = split(b)
    if split_b:
        return True, [a, b]

    return False, [a, b]

assert split([11, [2, 11]]) == (True, [[5, 6], [2, 11]])
assert split([9, [2, 11]]) == (True, [9, [2, [5, 6]]])
assert split([[9, 9], [9, 9]]) == (False, [[9, 9], [9, 9]])


def snailfish_sum(a, b):
    example = [a, b]
    changed = True
    while changed:
        changed, example, _, _ = explode(example)
        if not changed:
            changed, example = split(example)
    return example

assert reduce(snailfish_sum, [[1,1], [2,2], [3,3], [4,4]]) == [[[[1,1],[2,2]],[3,3]],[4,4]]


def magnitude(example):
    if isinstance(example, int):
        return example

    a, b = example
    return 3 * magnitude(a) + 2 * magnitude(b)

assert magnitude([[1,2],[[3,4],5]]) == 143
assert magnitude([[[[0,7],4],[[7,8],[6,0]]],[8,1]]) == 1384
assert magnitude([[[[1,1],[2,2]],[3,3]],[4,4]]) == 445
assert magnitude([[[[3,0],[5,3]],[4,4]],[5,5]]) == 791
assert magnitude([[[[5,0],[7,4]],[5,5]],[6,6]]) == 1137
assert magnitude([[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]]) == 3488


examples = [eval(line) for line in '''[[[0,[5,8]],[[1,7],[9,6]]],[[4,[1,2]],[[1,4],2]]]
[[[5,[2,8]],4],[5,[[9,9],0]]]
[6,[[[6,2],[5,6]],[[7,6],[4,7]]]]
[[[6,[0,7]],[0,9]],[4,[9,[9,0]]]]
[[[7,[6,4]],[3,[1,3]]],[[[5,5],1],9]]
[[6,[[7,3],[3,2]]],[[[3,8],[5,7]],4]]
[[[[5,4],[7,7]],8],[[8,3],8]]
[[9,3],[[9,9],[6,[4,9]]]]
[[2,[[7,7],7]],[[5,8],[[9,3],[0,2]]]]
[[[[5,2],5],[8,[3,7]]],[[5,[7,5]],[4,4]]]'''.splitlines()]
assert reduce(snailfish_sum, deepcopy(examples)) == [[[[6,6],[7,6]],[[7,7],[7,0]]],[[[7,7],[7,7]],[[7,8],[9,9]]]]
assert magnitude(reduce(snailfish_sum, deepcopy(examples))) == 4140


# 18-1
homework = [eval(line) for line in get_input(day=18)]
print(magnitude(reduce(snailfish_sum, deepcopy(homework))))

# 18-2
max_mag = 0
for a, b in permutations(homework, 2):
    a, b = deepcopy(a), deepcopy(b)

    mag = magnitude(snailfish_sum(a, b))
    if mag > max_mag:
        max_mag = mag
print(max_mag)
