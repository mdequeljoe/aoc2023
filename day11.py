import copy

def get_grid(x):
    return [list(x) for x in x.splitlines()]

def get_coords(grid, offset=1):
    x = []
    nr = range(len(grid))
    nk = range(len(grid[0]))
    for r in nr:
        for k in nk:
            if grid[r][k] == '#':
                x.append((r, k))
    empty_rows = [i for i in nr if i not in [r for r,k in x]]
    empty_cols = [i for i in nk if i not in [k for r,k in x]]
    for i in range(len(empty_rows)):
        rw = empty_rows[i] + i*offset
        x = [(r + 1*offset, k) if r > rw else (r, k) for r,k in x]
    for i in range(len(empty_cols)):
        cl = empty_cols[i] + i*offset
        x = [(r, k + 1*offset) if k > cl else (r, k) for r,k in x]
    return x

def mdist(c1, c2):
    x1, y1 = c1
    x2, y2 = c2
    return abs(x1 - x2) + abs(y1 - y2)


x = """...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#....."""
x = open("data/day11.txt").read()


grid = get_grid(x)
coords = get_coords(grid)
res = []
for i in range(len(coords)):
    for j in range(i+1,len(coords)):
        r = mdist(coords[i], coords[j])
        res.append(r)
print(sum(res))

# part 2
grid = get_grid(x)
coords = get_coords(grid, 1_000_000 - 1)
res = []
for i in range(len(coords)):
    for j in range(i+1,len(coords)):
        r = mdist(coords[i], coords[j])
        res.append(r)
print(sum(res))