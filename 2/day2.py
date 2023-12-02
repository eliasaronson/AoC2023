import regex as re
import numpy as np

def check_limits(line, maxs):
    for cubes in re.findall("(\d+) (\w+)", line):
        if int(cubes[0]) > maxs[cubes[1]]:
            return False
    return True

def part1(lines):
    maxs = {"red": 12, "green": 13, "blue": 14}
    possible = []

    for line in lines:
        game_id = int(re.search("(?<=Game )\d+", line)[0])
        if check_limits(line, maxs):
            possible.append(game_id)

    print(f"sum: {sum(possible)}, {possible=}")

def part2(lines):
    total = 0
    for line in lines:
        mins = {"red": 0, "green": 0, "blue": 0}
        for cubes in re.findall("(\d+) (\w+)", line):
            mins[cubes[1]] = max(int(cubes[0]), mins[cubes[1]])
        prod = np.prod(list(mins.values()))
        total += prod

    print(f"{total=}")

lines = open('input.txt').readlines()
part1(lines)
part2(lines)
