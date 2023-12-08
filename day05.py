
x = """seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4"""
x = open("data/day05.txt").read()

def get_map(x):
    return [[int(n) for n in x.split()] for x in x]

def get_inputs(x):
    maps = {}
    x = x.splitlines()
    seeds = x.pop(0)
    seeds = [int(x) for x in seeds.replace("seeds: ", '').split()]
    i = 0
    while True:
        if i == len(x):
            break
        line = x[i]
        if line == '':
            i += 1
            continue
        if 'map' in line:
            nm = line[:-1]
            m = []
            while True:
                i += 1
                if i == len(x):
                    break
                if x[i] == '':
                    break
                m.append(x[i])
            maps[nm] = get_map(m)
    return [seeds, maps]

def map_seed(seed, map):
    for line in map:
        dest, src, n = line
        if seed >= src and seed <= (src + n - 1):
            return dest + (seed - src)
    return seed

seeds, maps = get_inputs(x)
locations = []
map_order = ['seed-to-soil map',
        'soil-to-fertilizer map',
        'fertilizer-to-water map', 
        'water-to-light map', 
        'light-to-temperature map', 
        'temperature-to-humidity map', 
        'humidity-to-location map']
for s in seeds:
    for m in map_order:
        s = map_seed(s, maps[m])
    locations.append(s)
print(min(locations))

# part two
def seed_rng(seeds):
    res = []
    for i in range(len(seeds)):
        if i % 2 == 0:
            res.append((seeds[i], seeds[i] + seeds[i + 1] - 1))
    return res

def apply_rng(rng, map_line):
    dest, src, n = map_line
    s0 = src
    s1 = src + n - 1
    d0 = dest
    d1 = dest + n - 1
    res = {'mapped': [], 'unmapped': []}
    x0, x1 = rng
    # no overlap
    if (x0 < s0 and x1 < s0) or (x0 > s1):
        res['unmapped'].append((x0, x1))
    # partial overlap at beginning
    elif x0 < s0 and x1 >= s0 and x1 <= s1:
        res['mapped'].append((d0, d0 + (x1 - s0)))
        res['unmapped'].append((x0, src - 1))
    # partial overlap at end
    elif x0 >= s0 and x0 <= s1 and x1 > s1:
        res['mapped'].append((d0 + (x0 - s0), d1))
        res['unmapped'].append((s1 + 1, x1))
    # lapped on both sides
    elif x0 < s0 and x1 > s1:
        res['mapped'].append((d0, d1))
        res['unmapped'].append((x0, s0 - 1))
        res['unmapped'].append((s1 + 1, x1))
    # fully contained
    elif x0 >= s0 and x1 <= s1:
        res['mapped'].append((d0 + (x0 - s0), d0 + (x1 - s0)))
    return res

def map_seed_rng(seed_rng, map):
    out = []
    if isinstance(seed_rng, list):
        unmapped = seed_rng
    else:
        unmapped = [seed_rng]
    mapped = []
    for line in map:
        um = []
        for rng in unmapped:
            r = apply_rng(rng, line)
            um += r['unmapped']
            mapped += r['mapped']
        unmapped = um
    return mapped + unmapped
            
sr = seed_rng(seeds)
res = []
for r in sr:
    o = r
    for m in map_order:
        o = map_seed_rng(o, maps[m])
    res.append(min([x[0] for x in o]))
print(min(res))
