import re
with open('input.txt') as f:
    input = f.read()
    print('p01:', sum(
        [int(x) * int(y) for x, y in
         [re.findall(r'\d+', x) for x in
          re.findall(r'mul\(\d+,\d+\)', input)]]))
