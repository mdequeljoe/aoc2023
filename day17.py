from queue import PriorityQueue

def get_grid(x):
    return [[int(x) for x in list(x)] for x in x.splitlines()]

def in_grid(r, k, nr, nk):
    return r >= 0 and r < nr and k >= 0 and k < nk

def moves():
    return [(1, 0, 'd'), (0, 1, 'r'), (-1, 0, 'u'), (0, -1, 'l')]

def min_path(grid):
    nr = len(grid)
    nk = len(grid[0])
    seen = set()
    q = PriorityQueue()
    q.put((0, 0, 0, 0, None, []))
    invalid = {'d':'u', 'r':'l', 'l':'r', 'u':'d', None:None}

    while True:
        if q.empty():
            break

        score, r, k, n_steps, dir, past = q.get()
        if r == nr-1 and k == nk-1:
            return score
        
        if (r, k, dir, n_steps) in seen:
            continue
        seen.add((r,k,dir,n_steps))

        for dr, dk, new_dir in moves():
            if new_dir == invalid[dir]:
                continue

            r1 = r + dr
            k1 = k + dk
            
            if in_grid(r1, k1, nr, nk):
                if n_steps <= 3:
                    new_steps = 1
                    if dir == new_dir:
                        new_steps = n_steps + 1
                        if new_steps > 3:
                            continue
                    s = score + grid[r1][k1]
                    p = [p for p in past] + [(r, k, dir)]
                    q.put((s, r1, k1, new_steps, new_dir, p))

def min_path2(grid):
    nr = len(grid)
    nk = len(grid[0])
    seen = set()
    q = PriorityQueue()
    q.put((0, 0, 0, 0, 0, 'r', []))
    q.put((0, 0, 0, 0, 0, 'd', []))
    invalid = {'d':'u', 'r':'l', 'l':'r', 'u':'d', None:None}
    moves = {'d': (1, 0), 'r': (0, 1), 'u': (-1, 0), 'l': (0, -1)}

    while True:
        if q.empty():
            break

        score, r, k, n_steps, dir_cnt, dir, past = q.get()
        if r == nr-1 and k == nk-1 and dir_cnt >= 4:
            return score
        
        if (r, k, dir, n_steps, dir_cnt) in seen:
            continue
        seen.add((r,k,dir,n_steps, dir_cnt))

        if dir_cnt <= 3:
            dr, dk = moves[dir]
            r1, k1 = r + dr, k + dk 
            if in_grid(r1, k1, nr, nk):
                s = score + grid[r1][k1]
                p = [p for p in past] + [(r, k, n_steps, dir, dir_cnt)]
                q.put((s, r1, k1, n_steps + 1, dir_cnt + 1, dir, p))
            continue

        for key,val in moves.items():

            new_dir = key
            if new_dir == invalid[dir]:
                continue
            
            dr, dk = val
            r1 = r + dr
            k1 = k + dk
            
            if in_grid(r1, k1, nr, nk):
                if n_steps <= 10:
                    new_steps = 1
                    new_dir_cnt = 1
                    if dir == new_dir:
                        new_dir_cnt = dir_cnt + 1
                        new_steps = n_steps + 1
                        if new_steps > 10:
                            continue
                    s = score + grid[r1][k1]
                    p = [p for p in past] + [(r, k, dir, dir_cnt)]
                    q.put((s, r1, k1, new_steps, new_dir_cnt, new_dir, p))

x = """2413432311323
3215453535623
3255245654254
3446585845452
4546657867536
1438598798454
4457876987766
3637877979653
4654967986887
4564679986453
1224686865563
2546548887735
4322674655533"""
x = open("data/day17.txt").read()

grid = get_grid(x)
res = min_path(grid)
print(res)

#part 2
res = min_path2(grid)
print(res)

# x = """111111111111
# 999999999991
# 999999999991
# 999999999991
# 999999999991"""
# grid = get_grid(x)
# res = min_path2(grid)
# print(res)