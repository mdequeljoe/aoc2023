from skspatial.measurement import area_signed

def get_input(x):
    return[x.split(" ") for x in x.splitlines()]

def dig(ins):
    r, k = 0, 0
    moves = {'D': (1, 0), 'R': (0, 1), 'U': (-1, 0), 'L': (0, -1)}
    coords = [(r, k)]
    for line in ins:
        dir, len, color = line
        dr, dk = moves[dir]
        for i in range(int(len)):
            r += dr
            k += dk
            coords.append((r,k))
    return coords

mem = {'col-rows':{}, 'row-cols':{}}

def in_grid(r, k, coords):
    if r not in mem['row-cols'].keys():
        cl = sorted([cl for rw,cl in coords if rw == r])
        mem['row-cols'][r] = [cl[0], cl[-1]]
    else:
        cl = mem['row-cols'][r]
    if k not in mem['col-rows'].keys():
        rw = sorted([rw for rw,cl in coords if cl == k])
        mem['col-rows'][k] = [rw[0], rw[-1]]
    else:
        rw = mem['col-rows'][k]
    return r >= rw[0] and r <= rw[-1] and k >= cl[0] and k <= cl[-1]
    

def fill(coords, r, k):
    q = [(r,k)]
    seen = set(coords)
    moves = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    while q:
        r,k = q.pop()
        if (r,k) in seen:
            continue
        seen.add((r,k))
        for m in moves:
            dr, dk = m
            r1, k1 = r + dr, k + dk
            if in_grid(r1,k1, coords):
                q.append((r1, k1))
    return seen
    
    
x = """R 6 (#70c710)
D 5 (#0dc571)
L 2 (#5713f0)
D 2 (#d2c081)
R 2 (#59c680)
D 2 (#411b91)
L 5 (#8ceee2)
U 2 (#caa173)
L 1 (#1b58a2)
U 2 (#caa171)
R 2 (#7807d2)
U 3 (#a77fa3)
L 2 (#015232)
U 2 (#7a21e3)"""
x = open("data/day18.txt").read()

k = get_input(x)
d = dig(k)
res = fill(d, 1, 1)
print(len(res))

# part two
def perimeter_directions(x):
    forced_turns = ['RU', 'LD', 'DR', 'UL']
    rounding_corners = ['RD', 'LU', 'DL', 'UR']
    res = []
    for i in range(len(x)):
        dir, n, color = x[i]
        n = int(n)
        if i == 0:
            prev = "U"
        else:
            prev = x[i - 1][0]
        if i == len(x) - 1:
            ahead = 'R'
        else:
            ahead = x[i + 1][0]
        
        prev_turn = prev + dir
        next_turn = dir + ahead
        
        if prev_turn in rounding_corners and next_turn in rounding_corners:
            n += 1
        elif prev_turn in rounding_corners and next_turn in forced_turns:
            n = n
        elif prev_turn in forced_turns and next_turn in forced_turns:
            n -= 1
        elif prev_turn in forced_turns and next_turn in rounding_corners:
            n = n
        res.append([dir, n])
        
    return res
            
def get_input2(x):
    res = []
    directions = ['R', 'D', 'L', 'U']
    for line in x.splitlines():
        dir, n, val = line.split(" ")
        val = val.replace("(", "")
        val = val.replace(")", "")
        n, dir = int(val[1:-1], 16), int(val[-1])
        dir = directions[dir]
        res.append([dir, n, line])
    return res

def dig2(ins):
    r, k = 0, 0
    moves = {'D': (1, 0), 'R': (0, 1), 'U': (-1, 0), 'L': (0, -1)}
    coords = [(r, k)]
    for line in ins:
        dir, len = line
        dr, dk = moves[dir]
        dr, dk = dr * len, dk * len
        r, k = r + dr, k + dk
        coords.append((r, k))
    return coords

k = get_input2(x)
per = perimeter_directions(k)
d2 = dig2(per)
res = int(area_signed(d2))
print(abs(res))

# 2nd way (from:  https://stackoverflow.com/questions/67114437/calculate-area-of-rectilinear-polygon-in-c)
x = 0
y = 0
A = 0
d = 0
for line in per:
    dir, l = line
    d = int(l)
    if dir == "L":
        x += d
        A += d * y
    elif dir == "R":
        x -= d
        A -= d * y
    elif dir == "U":
        y += d
    elif dir == "D":
        y -= d

if A < 0:
    A *= -1
# print(A)

