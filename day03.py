import re
x = """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598.."""
x = open('data/day03.txt').read()

grid = [list(x.replace(".", " ")) for x in x.split("\n")]

num = [re.sub(r'\D', ' ', x).split(" ") for x in x.split("\n")]
num = [[x for x in x if x.isdigit()] for x in num]
for row in range(len(num)):
    i = 0
    for n in num[row]:
        nk = len(n)
        cnt = 0
        while True:
            if grid[row][i].isdigit():
                grid[row][i] = n
                cnt += 1
            i += 1
            if cnt == nk or i > len(grid[row]):
                break


def get_parts(grid, row, col):
    o = [-1, 0, 1]
    nr = len(grid)
    nk = len(grid[0])
    vals = []
    for r in o:
        rw = row + r
        if rw < 0 or rw >= nr:
            continue
        for k in o:
            cl = col + k
            if cl < 0 or cl >= nk:
                continue
            val = grid[rw][cl]
            if val.isdigit():
                vals.append(int(val))
    return list(set(vals))

s = 0
for r in range(len(grid)):
    for k in range(len(grid[0])):
        v = grid[r][k]
        if not v.isdigit() and v != ' ':
            s += sum(get_parts(grid, r, k))
print(s)

# part 2
s = 0
for r in range(len(grid)):
    for k in range(len(grid[0])):
        v = grid[r][k]
        if v == "*":
            g = get_parts(grid, r, k)
            if len(g) == 2:
                s += g[0] * g[1]
print(s)
