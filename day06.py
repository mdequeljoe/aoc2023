x = """Time:      7  15   30
Distance:  9  40  200"""
x = open("data/day06.txt").read()

def get_input(x):
    t,d = x.splitlines()
    t = [int(n) for n in t.replace('Time: ', '').split()]
    d = [int(n) for n in d.replace('Distance: ', '').split()]
    res = []
    for i in range(len(t)):
        res.append((t[i], d[i]))
    return res

def get_wins(x):
    t,d = x
    n_wins = 0
    for i in range(t + 1):
        res = (t - i) * i
        if res > d:
            n_wins += 1
    return n_wins

x = get_input(x)

res = 1
for x in x:
    res *= get_wins(x)
print(res)

# part two
print(get_wins((53837288, 333163512891532)))