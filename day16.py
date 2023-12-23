
def get_grid(x):
    return [list(x) for x in x.splitlines()]

def next_move(grid, coord, dir):
    r,k = coord
    if dir == 'r':
        k += 1
    elif dir == 'l':
        k -= 1
    elif dir == 'd':
        r += 1
    elif dir == 'u':
        r -= 1
    if r < 0 or k < 0 or r == len(grid) or k == len(grid[r]):
        return None
    return (r, k)

def count_tiles(grid, s = [[(0, 0), 'r']]):

    seen_splits = []
    passed = set()

    while True:
        if len(s) == 0:
            break

        coord, dir = s.pop()
        passed.add(coord)
        r,k = coord
        val = grid[r][k]
        is_split = False
        if val == '.':
            next_dir = dir
        elif val == '-': 
            if dir in ['r', 'l']:
                next_dir = dir
            else:
                is_split = True
                next_dir = ['l', 'r']
        elif val == '|':
            if dir in ['u', 'd']:
                next_dir = dir
            else:
                is_split = True
                next_dir = ['u', 'd']
        elif val == '\\':
            if dir == 'u':
                next_dir = 'l'
            elif dir == 'd':
                next_dir = 'r'
            elif dir == 'l':
                next_dir = 'u'
            else:
                next_dir = 'd'
        elif val == '/':
            if dir == 'u':
                next_dir = 'r'
            elif dir == 'd':
                next_dir = 'l'
            elif dir == 'l':
                next_dir = 'd'
            else:
                next_dir = 'u'
        
        # print(coord, val, dir, 'next_dir=', next_dir)

        if is_split:
            # print('split at:', coord)
            seen_splits.append(coord)
            for d in next_dir:
                cd = next_move(grid, coord, d)
                if cd is not None and cd not in seen_splits:
                    s.append([cd, d])
        else:
            cd = next_move(grid, coord, next_dir)
            if cd is not None and cd not in seen_splits:
                s.append([cd, next_dir])

    return len(passed)

       

x = open("data/day16.txt").read()
# x = open("data/day16_test.txt").read()
grid = get_grid(x)
res = count_tiles(grid)


s = 0
nr = len(grid)
nk = len(grid[0])
for r in range(nr):
    res = count_tiles(grid, [[(r, 0), 'r']])
    s = max(res, s)
    res = count_tiles(grid, [[(r, nk-1), 'l']])
    s = max(res, s)
for k in range(nk):
    res = count_tiles(grid, [[(0, k), 'd']])
    s = max(res, s)
    res = count_tiles(grid, [[(nr-1, k), 'u']])
    s = max(res, s) 

print(s)