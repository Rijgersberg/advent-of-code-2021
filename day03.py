from aoc import get_input

from collections import Counter


numbers = get_input(day=3)
transposed = list(map(list, zip(*numbers)))

# 3-1
gamma = []
epsilon = []
for bits in transposed:
    most = Counter(bits).most_common(1)[0][0]
    least = '1' if most == '0' else '0'
    gamma.append(most)
    epsilon.append(least)

gamma = int(''.join(gamma), 2)
epsilon = int(''.join(epsilon), 2)
print(gamma * epsilon)


# 3-2
def eliminate(bits, remaining, use_most, tie):
    bits_to_consider = [(i, b) for i, b in enumerate(bits) if i in remaining]

    most, count = Counter([b for i, b in bits_to_consider]).most_common(1)[0]
    least = '1' if most == '0' else '0'

    if len(bits_to_consider) % 2 != 0 or count != len(bits_to_consider) // 2:
        remaining -= {i for i, b in bits_to_consider if b == (least if use_most else most)}
    else:
        remaining -= {i for i, b in bits_to_consider if b == ('1' if tie == '0' else '0')}
    return remaining


oxygen = {*range(len(numbers))}
co2 = {*range(len(numbers))}
for bits in transposed:
    if len(oxygen) > 1:
        oxygen = eliminate(bits, oxygen, use_most=True, tie='1')
    if len(co2) > 1:
        co2 = eliminate(bits, co2, use_most=False, tie='0')

final_oxygen = int(numbers[list(oxygen)[0]], 2)
final_co2 = int(numbers[list(co2)[0]], 2)
print(final_oxygen * final_co2)

