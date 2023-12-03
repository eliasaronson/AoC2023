import numpy as np
import re

file = "input.txt"
schem = np.loadtxt(file, dtype=str, comments=None)
schem = schem.view('U1').reshape((schem.size, -1))

lines = open(file).readlines()
total = 0

for x, y in zip(*np.where(schem == '*')):
    roi = schem[x-1:x+2, y-1:y+2].view('U3').reshape(-1)
    matches = []
    for idx, line in enumerate(roi):
        for match in re.finditer("\d+", line):
            matches.append((x - 1 + idx, y - 1 + match.start()))

    if len(matches) > 1:
        mul = 1
        for x, y in matches:
            for match in re.finditer("\d+", lines[x]):
                if match.span()[0] <= y <= match.span()[1]:
                    mul *= int(match.group())
                    break
        total += mul
        
print(f"{total=}")
