import numpy as np
from scipy import signal
import re

file = "input.txt"
schem = np.loadtxt(file, dtype=str, comments=None)
schem = schem.view('U1').reshape((schem.size, -1))

r = re.compile('(\d|\.)')
vmatch = np.vectorize(lambda x:bool(r.match(x)))
sel = vmatch(schem)

map = np.ones(schem.shape)
map[sel] = 0
conv = signal.convolve2d(map, np.ones((3, 3)), mode="same")

total = 0

lines = open(file).readlines()
for x_idx, line in enumerate(lines):
    for match in re.finditer("\d+", line):
        if np.sum(conv[x_idx, match.span()[0]:match.span()[1]]) > 0:
            total += int(match.group())

print(f"{total=}")

