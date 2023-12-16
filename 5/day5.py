import re
from dataclasses import dataclass


@dataclass
class map_s:
    fro: int
    to: int
    len: int

lines = open("input.txt").readlines()

seeds = re.sub("seeds: ", "", lines[0])
seeds = list(map(int, seeds.split()))

map = []
maps = []
for line in lines[3:]:
    if line == lines[1]:
        continue
    if re.search("\d", line):
        sp = line.split()
        map.append(map_s(int(sp[1]), int(sp[0]), int(sp[2])))
    else:
        maps.append(map)
        map = []

maps.append(map)

locs = []
for seed in seeds:
    # print("\nstart:", seed)
    for map in maps:
        for rang in map:
            if rang.fro <= seed <= rang.fro + rang.len:
                seed = rang.to + seed - rang.fro  
                # print("found:", seed, "range:", rang)
                break
        # print("Not in range:", seed)
    locs.append(seed)

            

print(seeds)
print(maps)
print(f"{min(locs)}")
