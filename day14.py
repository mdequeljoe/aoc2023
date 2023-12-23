
def get_grid(x):
    return [list(x) for x in x.splitlines()]

def tilt_board(coords, cubes, dir, nr, nk):
    if dir == 'N':
        coords = sorted(coords)
    elif dir == 'S':
        coords = sorted(coords, reverse=True)
    elif dir == 'W':
        coords = sorted(coords, key=lambda x: x[1])
    else:
        coords = sorted(coords, key=lambda x: x[1], reverse=True)
    new_coords = []
    while True:
        if len(coords) == 0:
            break
        r, k = coords.pop(0)
        r1, k1 = r, k
        r0, k0 = r, k
        while True:
            if (r1, k1) in cubes \
                or (r1, k1) in coords \
                or (r1, k1) in new_coords:
                    new_coords.append((r0, k0))
                    break

            if dir == 'N' and r1 == 0 \
                or dir == 'S' and r1 == (nr-1) \
                or dir == 'W' and k1 == 0 \
                or dir == 'E' and k1 == (nk-1):
                    new_coords.append((r1, k1))
                    break
            r0, k0 = r1, k1
            if dir == 'N':
                r1 -= 1
            elif dir == 'S':
                r1 += 1
            elif dir == 'W':
                k1 -= 1
            else:
                k1 += 1
    return new_coords

def score_grid(coords, nr):
    s = 0
    for i in range(nr):
        nrocks = len([x for x in coords if x[0] == i])
        s += nrocks * (nr - i)
    return s

def tilt_cycle(coords, cubes, n, nr, nk):
    seen = {}
    for _ in range(n):
        for dir in ['N', 'W', 'S', 'E']:
            if tuple(coords) in seen.keys():
                coords = seen[tuple(coords)]
                continue
            else:
                seen[tuple(coords)] = tilt_board(coords, cubes, dir, nr, nk)
                coords = seen[tuple(coords)]
        if _ % 100 == 0:
            print(_, score_grid(coords, nr))
    return coords


x = """O....#....
O.OO#....#
.....##...
OO.#O....O
.O.....O#.
O.#..O.#.#
..O..#O..O
.......O..
#....###..
#OO..#...."""
x = open("data/day14.txt").read()
g = get_grid(x)
coords = []
cubes = []
for r in range(len(g)):
    for k in range(len(g[r])):
        if g[r][k] == 'O':
            coords.append((r,k))
        elif g[r][k] == '#':
            cubes.append((r,k))
nr = len(g)
nk = len(g[0])

# part one
ans = tilt_board([k for k in coords], cubes, 'N', nr, nk)
print(score_grid(ans, nr))

# part two
# a = tilt_cycle(coords, cubes, 1_000_000_000, nr, nk)

# 5_000_000 
# 64,69,68,65,65,69,63

x = 83500
o = [91332, 91320, 91306, 91286, 91270, 91278, 91295, 91317, 91333]
id = ((1_000_000_000 - 83400-1) // 100) % len(o)
print(o[id])
