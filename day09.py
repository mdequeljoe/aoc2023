x = """0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45"""
x = open("data/day09.txt").read()

def get_input(x):
    return [[int(x) for x in x.split()] for x in x.splitlines()]

def diff(x):
    return [x[i] - x[i -1] for i in range(1, len(x))]

def find_num(x):
    res = [x]
    while True:
        d = diff(res[-1])
        res.append(d)
        if all([d == 0 for d in d]):
            break
    res.reverse()
    for i in range(1, len(res)):
        res[i].append(res[i-1][-1] + res[i][-1])
    return res[-1][-1]

x = get_input(x)
res = [find_num(x) for x in x]
print(sum(res))

# part two
def find_num2(x):
    res = [x]
    while True:
        d = diff(res[-1])
        res.append(d)
        if all([d == 0 for d in d]):
            break
    res.reverse()
    for i in range(1, len(res)):
        res[i] = [ res[i][0] - res[i-1][0]  ] + res[i]
    return res[-1][0]

x = open("data/day09.txt").read()
x = get_input(x)
res = [find_num2(x) for x in x]
print(sum(res))
