
x = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"""

limits = {'red': 12, 'green': 13, 'blue':14}

x = open('data/day02.txt').read()
games = [x.split(": ") for x in x.split("\n")]
id = 1
sum_valid = 0
for g in games:
    sets = g[1].split("; ")
    is_valid = True
    for s in sets:
        s = [s.split(" ") for s in s.split(", ")]
        for cnt, color in s:
            if limits[color] < int(cnt):
                is_valid = False
                break
        if not is_valid:
            break
    if is_valid:
        print(id)
        sum_valid += id
    id += 1
print(sum_valid)

# part 2
sum_power = 0
for g in games:
    sets = g[1].split("; ")
    cubes = {'green': 0, 'red': 0, 'blue': 0}
    for s in sets:
        s = [s.split(" ") for s in s.split(", ")]
        for cnt, color in s:
            cubes[color] = max(cubes[color], int(cnt))
    sum_power += cubes['green'] * cubes['red'] * cubes['blue']

print(sum_power)