from collections import Counter
from itertools import permutations, product
x = """32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483"""
x = open("data/day07.txt").read()

def get_input(x):
    res = {}
    for x in x.splitlines():
        card, bid = x.split(" ")
        res[card] = {'hand': list(card), 'bid' : int(bid), 'score': None}
    return res

def get_cards(joker_rule=False):
    cards = {}
    card_nms = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']
    if joker_rule:
        card_nms = ['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J']
    n = len(card_nms)
    for i in range(n):
        cards[card_nms[i]] = n - i
    return cards

def card_values(hand, cards):
    return [cards[h] for h in hand]

def score_hand(hand):
    cnt = Counter(hand).most_common()
    top = cnt[0][1]
    if top == 5:
        h = 7
    elif top == 4:
        h = 6
    elif top == 3 and cnt[1][1] == 2:
        h = 5
    elif top == 3 and len(cnt) == 3:
        h = 4
    elif top == 2 and cnt[1][1] == 2:
        h = 3
    elif top == 2 and len(cnt) == 4:
        h = 2
    elif len(cnt) == 5:
        h = 1
    return h 

x = get_input(x) 
cards = get_cards()
for k,v in x.items():
    s = score_hand(v['hand'])
    v['score'] = tuple([s] + card_values(v['hand'], cards))

res = dict(sorted(x.items(), key=lambda v: v[1]['score']))
total = 0
bids = [v['bid'] for k,v in res.items()]
for i in range(len(bids)):
    total += bids[i] * (i + 1)
print(total)

# part 2
def score2(hand):
    j_id = [c for c,v in enumerate(hand) if v == 'J']
    h = [h for h in hand if h != 'J']
    if len(j_id) == 0 or len(h) == 0:
        return score_hand(hand)
    pm = list(product(h, repeat=len(j_id)))
    s = []
    for p in pm:
        new_hand = [h for h in hand]
        for i in range(len(j_id)):
            new_hand[j_id[i]] = p[i]
        s.append(score_hand(new_hand))
    s = sorted(s)
    return s[-1]

x = open("data/day07.txt").read()
x = get_input(x)
cards = get_cards(True)
for k,v in x.items():
    s = score2(v['hand'])
    v['score'] = tuple([s] + card_values(v['hand'], cards))

res = dict(sorted(x.items(), key=lambda v: v[1]['score']))
h = [k for k,v in res.items()]
total = 0
bids = [v['bid'] for k,v in res.items()]
for i in range(len(bids)):
    total += bids[i] * (i + 1)
print(total)

