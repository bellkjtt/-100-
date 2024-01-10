import sys
from itertools import combinations

r,g,b=map(int,sys.stdin.readline().split())
print(r,g,b)

def rgb_combination(r, g, b):
    if r == 0 and g == 0 and b == 0:
        return []
    elif r == 0:
        return rgb_combination(g, b)
    elif g == 0:
        return rgb_combination(r, b)
    elif b == 0:
        return rgb_combination(r, g)
    else:
        return [
            (r, g, b),
            rgb_combination(r - 1, g, b),
            rgb_combination(r, g - 1, b),
            rgb_combination(r, g, b - 1),
        ]


combinations = rgb_combination(2, 2, 2)
for combination in sorted(combinations):
    print(combination)
print(len(combinations))

