
x = open('data/day01.txt').read()
x = [list(x) for x in x.split('\n')]
s = 0
for l in x:
    n = []
    for k in l:
        if k.isdigit():
            n.append(k)
    s += int(n[0] + n[-1]) 
print(s)

# part 2
x = open('data/day01.txt').read()
x = [x for x in x.split('\n')]
w = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
w = w + [str(c + 1) for c,v in enumerate(w)]
s = 0
for k in x:
    first_pos = [k.find(s) for s in w]
    last_pos = [k.rfind(s) for s in w]

    first = [n for n in first_pos if n > -1]
    fp = first_pos.index(min(first)) % 9 + 1
    lp = last_pos.index(max(last_pos)) % 9 + 1
    s += int(str(fp) + str(lp)) 
print(s)