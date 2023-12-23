import copy
def get_input(x):
    res = []
    r = []
    for line in x.splitlines():
        if line == '':
            res.append(r)
            r = []
        else:
            r.append(list(line))
    res.append(r)
    return res

def transpose(x):
    return [[row[i] for row in x] for i in range(len(x[0]))]

# a - upper or lhs
def find_reflection(g):

    for i in range(1, len(g)):
        a = [x for x in g[:i]]
        b = [x for x in g[i:]]
        reflected = True
        while True:
            if len(a) == 0 or len(b) == 0:
                break
            ra = a.pop()
            rb = b.pop(0)
            if ra != rb:
                reflected = False
                break
        if reflected:
            return(i)
    return -1


def score_reflection(g):
    rf = find_reflection(g)
    if rf > -1:
        return rf * 100
    rf = find_reflection(transpose(g))
    if rf > -1:
        return rf

x = """#.##..##.
..#.##.#.
##......#
##......#
..#.##.#.
..##..##.
#.#.##.#.

#...##..#
#....#..#
..##..###
#####.##.
#####.##.
..##..###
#....#..#"""
x = open("data/day13.txt").read()
x = get_input(x)
s = 0
for g in x:
    s += score_reflection(g)
print(s)

# part two
def find_reflection2(g):
    for i in range(1, len(g)):
        a = [x for x in g[:i]]
        b = [x for x in g[i:]]
        reflected = True
        smudge_found = False
        while True:
            if len(a) == 0 or len(b) == 0:
                break
            ra = a.pop()
            rb = b.pop(0)
            diff = [int(ra[j] != rb[j]) for j in range(len(ra))]
            total_diff = sum(diff)
            if total_diff > 1:
                reflected = False
                break
            if total_diff == 1:
                smudge_found = True
        if reflected and smudge_found:
            return(i)
    return -1

def second_reflection(g):
    rf = find_reflection2(g)
    if rf > -1:
        return rf * 100
    rf = find_reflection2(transpose(g))
    if rf > -1:
        return rf

s = 0
for g in x:
    s += second_reflection(g)
print(s)