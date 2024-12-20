import math
import copy


def is_valid1(x: list) -> bool:
    diffs = [x[i - 1] - x[i] for i in range(1, len(x))]
    previous_diff = math.copysign(1, diffs[0])
    for v in diffs:
        if abs(v) == 0 or abs(v) > 3 or (s := math.copysign(1, v)) != previous_diff:
            return False
    previous_diff = s
    return True


def mix(x: list) -> list:
    a = []
    for i in range(len(x)):
        c = copy.copy(x)
        c.pop(i)
        a.append(c)
    a.append(x)
    return a


def is_valid2(x: list) -> bool:
    a = []
    mix_v = mix(x)
    for v in mix_v:
        a.append(is_valid1(v))

    return sum(filter(lambda x: x, a)) >= 1


with open('input.txt') as f:
    input = [list(map(int, x.split())) for x in f.read().splitlines()]
    print('p01:', len(list(filter(is_valid1, input))))
    print('p02:', len(list(filter(is_valid2, input))))
