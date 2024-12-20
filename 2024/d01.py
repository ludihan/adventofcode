with open('input.txt') as f:
    lines = [list(map(int, x.split())) for x in f.read().splitlines()]
    left_list = sorted([x[0] for x in lines])
    right_list = sorted([x[1] for x in lines])

    print('p01:', sum([abs(left - right) for left, right in zip(left_list, right_list)]))
    print('p02:', sum([x * right_list.count(x) for x in left_list]))
