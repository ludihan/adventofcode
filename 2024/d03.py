import re
from typing import List


def remove_disabled_instructions(input: List[str]) -> List[str]:
    a = []
    do = True
    for x in input:
        if x == "do()":
            do = True
            continue
        if x == "don't()":
            do = False
            continue

        if do and x != "do()" and x != "don't()":
            a.append(x)

    return a


with open("input.txt") as f:
    input = f.read()
    print(
        "p01:",
        sum(
            [
                int(x) * int(y)
                for x, y in [
                    re.findall(r"\d+", x) for x in re.findall(r"mul\(\d+,\d+\)", input)
                ]
            ]
        ),
    )
    print(
        "p02:",
        sum(
            [
                int(x) * int(y)
                for x, y in [
                    re.findall(r"\d+", x)
                    for x in remove_disabled_instructions(
                        re.findall(r"mul\(\d+,\d+\)|do\(\)|don't\(\)", input)
                    )
                ]
            ]
        ),
    )
