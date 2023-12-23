
def hash(str):
    s = 0
    for i in range(len(str)):
        s += ord(str[i])
        s *= 17
        s = s % 256
    return s

x = "rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7"
x = open("data/day15.txt").read()

res = [hash(s) for s in x.split(",")]
print(sum(res))

# part two
boxes = [{'label':[], 'value':[]} for _ in range(255 + 1)]
for el in x.split(","):
    if "=" in el:
        lab, val = el.split("=")
        id = hash(lab)
        if lab in boxes[id]['label']:
            lab_id = boxes[id]['label'].index(lab)
            boxes[id]['value'][lab_id] = int(val)
        else:
            boxes[id]['label'].append(lab)
            boxes[id]['value'].append(int(val))
    else:
        lab = el[:-1]
        id = hash(lab)        
        if lab in boxes[id]['label']:
            lab_id = boxes[id]['label'].index(lab)
            boxes[id]['label'].pop(lab_id)
            boxes[id]['value'].pop(lab_id)

res = 0
for i in range(len(boxes)):
    bx = boxes[i]
    if len(bx['label']) == 0:
        continue
    power = [(i + 1) * (j + 1) * bx['value'][j] for j in range(len(bx['value']))]
    res += sum(power)
print(res)
