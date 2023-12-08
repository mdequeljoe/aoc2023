import math
x = """RL

AAA = (BBB, CCC)
BBB = (DDD, EEE)
CCC = (ZZZ, GGG)
DDD = (DDD, DDD)
EEE = (EEE, EEE)
GGG = (GGG, GGG)
ZZZ = (ZZZ, ZZZ)"""

x = open("data/day08.txt").read()

def get_input(x):
    x = x.splitlines()
    dirs = list(x[0].strip())
    mp = {}
    for i in range(2, len(x)):
        lh, rh = x[i].split(" = ")
        rh = rh.replace("(", '')
        rh = rh.replace(')', '')
        rh = rh.replace(',', '')
        mp[lh] = rh.split(" ")
    return [dirs, mp]

def travel_network(x):
    dirs, nw = x
    n = len(dirs)
    current = 'AAA'
    i = 0
    steps = 0
    while True:
        steps += 1
        d = dirs[i]
        id = 0
        if d == 'R':
            id = 1
        current = nw[current][id]
        if current == 'ZZZ':
            break
        i = (i + 1) % n
    return steps

x = get_input(x)
res = travel_network(x)
print(res)

# part two
def next_node(k, nw, d):
    id = 0
    if d == 'R':
        id = 1
    return nw[k][id]

def travel_network2(node, dirs, nw):
    dirs, nw = x
    n = len(dirs)
    i = 0
    steps = 0
    while True:
        steps += 1
        node = next_node(node, nw, dirs[i])
        if node[2] == 'Z':
            break
        i = (i + 1) % n
    return steps

dirs, nw = x
nodes = [k for k in nw.keys() if k[2] == 'A']
steps = [travel_network2(nd, dirs, nw) for nd in nodes]
print(math.lcm(*steps))
