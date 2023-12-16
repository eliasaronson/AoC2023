import numpy as np

def in_bound(pos, map):
    return -1 < pos.real < map.shape[0] and  -1 < pos.imag < map.shape[1]

def im_to_tuple(vel):
    return (int(vel.real), int(vel.imag))

def turn(pos, dir, map):
    tile = map[*im_to_tuple(pos)]
    match tile:
        case '.':
            return [dir]
        case '/':
            return [complex(-dir.imag, -dir.real)]
        case '\\':
            return [complex(dir.imag, dir.real)]
        case '-':
            if abs(dir.imag) == 1:
                return [dir]
            return [complex(0, 1), complex(0, -1)]
        case '|':
            if abs(dir.real) == 1:
                return [dir]
            return [complex(-1, 0), complex(1, 0)]
        case _:
            print("Warning. Unkown tile:", tile)
            return [dir]


def ray_trace(map, poss, dirs):
    map_org = map.copy()
    visited = set() # Poor mans cache

    while len(poss):
            pos = poss.pop() # (y, x)
            dir = dirs.pop()

            while in_bound(pos, map_org):
                ndirs = turn(pos, dir, map_org)
                for i in range(1, len(ndirs)):
                    poss.append(pos)
                    dirs.append(ndirs[i])

                dir = ndirs[0]
                map[*im_to_tuple(pos)] = '*'
                pos += dir
                if (pos, dir) in visited:
                    break

                visited.add((pos, dir))

    enegergized = np.where(map == '*')[0]
    return enegergized.shape[0]

# Load input
file = "input.txt"
map = np.loadtxt(file, dtype=str, comments=None)
map = map.view('U1').reshape((map.size, -1))

# Part 1
res = ray_trace(map.copy(), [complex(0, 0)], [complex(0, 1)])
print(f"Part 1: {res}")

# Part 2
steps = [complex(0, 1), complex(1, 0), complex(1, 0), complex(0, 1)]
starts = [complex(0, 0), complex(0, 0), complex(0, map.shape[1] - 1), complex(map.shape[0] - 1, 0)]
dirss = [complex(1, 0), complex(0, 1), complex(0, -1), complex(-1, 0)]
res = np.zeros(map.shape[0] * 2 + map.shape[1] *2)

idx = 0
for side in range(4):
    start_pos = starts[side]
    while(in_bound(start_pos, map)):
        res[idx] = ray_trace(map.copy(), [start_pos], [dirss[side]])
        idx += 1
        start_pos += steps[side]

print(np.max(res))
