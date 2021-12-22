from pprint import pprint
from functools import reduce
from itertools import *
from collections import defaultdict
import json

aunts = {}
# names = set()
i = 1
for l in open("input.txt","r").readlines():
    si = l.index(":")
    aunts[i] = { p:int(e) for p,e in [s.strip().split(":") for s in l[si+1:].strip().split(",")]}
    i += 1

pprint(aunts)

find = {
"children": 3,
"cats": 7,
"samoyeds": 2,
"pomeranians": 3,
"akitas": 0,
"vizslas": 0,
"goldfish": 5,
"trees": 3,
"cars": 2,
"perfumes": 1
}

matches = []
# part 2
fewer = ["pomeranians","goldfish"]
greater = ["cats","trees"]

for a in aunts:
    items = aunts[a]
    count = 0
    for i in find:
        # part 2
        if i in fewer and i in items and items[i] < find[i]:
            count += 1
        if i in greater and i in items and items[i] > find[i]:
            count += 1
        #--
        elif i in items and items[i] == find[i]:
            count += 1
    if count == len(items.keys()):
        matches.append((a,count))

pprint(matches)
matches.sort(key=lambda t: t[1])
print(matches[-1][0])
