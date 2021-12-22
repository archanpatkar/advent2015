from pprint import pprint
from functools import reduce
from collections import defaultdict

data = []
for l in open("input.txt","r").readlines():
    l = l.split(" ")
    if l[0] == "turn": 
        com = 1 if l[1] == "on" else 0
        data.append((com,tuple(map(int,l[2].split(","))),tuple(map(int,l[4].split(",")))))
    else: data.append((2,tuple(map(int,l[1].split(","))),tuple(map(int,l[3].split(",")))))
pprint(data)

# part 1
# lights = defaultdict(int)
# for inst in data:
#     if inst[0] == 2:
#         x1, y1 = inst[1]
#         x2, y2 = inst[2]
#         for x in range(x1,x2+1):
#             for y in range(y1,y2+1):
#                 lights[(x,y)] = not lights[(x,y)]
#     else:
#         x1, y1 = inst[1]
#         x2, y2 = inst[2]
#         for x in range(x1,x2+1):
#             for y in range(y1,y2+1):
#                 lights[(x,y)] = inst[0]

# print(sum([lights[l] for l in lights]))

lights = defaultdict(int)
for inst in data:
    if inst[0] == 2:
        x1, y1 = inst[1]
        x2, y2 = inst[2]
        for x in range(x1,x2+1):
            for y in range(y1,y2+1):
                lights[(x,y)] += 2
    else:
        x1, y1 = inst[1]
        x2, y2 = inst[2]
        for x in range(x1,x2+1):
            for y in range(y1,y2+1):
                lights[(x,y)] += 1 if inst[0] else -1
                if lights[(x,y)] < 0: lights[(x,y)] = 0

print(sum([lights[l] for l in lights]))