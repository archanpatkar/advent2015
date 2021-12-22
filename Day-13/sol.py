from pprint import pprint
from functools import reduce
from itertools import *
from collections import defaultdict

data = {}
names = set()
for l in open("input.txt","r").readlines():
    l = l.strip().split(" ")
    n = 1
    if l[2] == "lose": n = -1
    data[(l[0],l[-1][:-1])] = n * int(l[3])
    names.add(l[0])

pprint(data)
pprint(names)

# part 2
for n in names: 
    data[("archan",n)] = 0
    data[(n,"archan")] = 0
names.add("archan")
#---

changes = []
for p in permutations(names):
    count = 0
    for i in range(len(p)-1): 
        count += data[(p[i],p[i+1])]
        count += data[(p[i+1],p[i])]
    count += data[(p[0],p[-1])]
    count += data[(p[-1],p[0])]
    changes.append(count)
print(max(changes))