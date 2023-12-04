
x = """Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"""
x = open('data/day04.txt').read()

def get_cards(x):
    return set(int(x) for x in x.split())

x = [x.split(": ")[1] for x in x.split("\n")]
x = [x.split(" | ") for x in x]
total = 0
for line in x:
    win = get_cards(line[0])
    hand = get_cards(line[1])
    s = hand.intersection(win)
    n = len(s)
    if n:
        total += 1*2**(n-1)
print(total)

# part 2
cards = {i:1 for i in range(len(x))}
for i in range(len(x)):
    line = x[i]
    win = get_cards(line[0])
    hand = get_cards(line[1])
    s = hand.intersection(win)
    n = len(s)
    for j in range(n):
        cards[i + j + 1] += cards[i]
print(sum([v for k,v in cards.items()]))
