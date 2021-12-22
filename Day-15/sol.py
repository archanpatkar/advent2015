from pprint import pprint
from functools import reduce
from itertools import *
from collections import defaultdict

props = {}
names = set()
for l in open("input.txt","r").readlines():
    l = l.strip().split(":")
    props[l[0]] = { p:int(e) for p,e in [s.strip().split(" ") for s in l[1].strip().split(",")]}
    names.add(l[0])

pprint(names)
pprint(props)

numbers = range(0,100)
cookie_score = []
for ar in combinations(numbers,len(names)):
    if sum(ar) == 100:
        for nc in permutations(names):
                # print(ar)
                capacity = 0
                durability = 0
                flavor = 0
                texture = 0
                calories = 0
                i = 0
                for p in nc:
                    n = ar[i]
                    i += 1
                    capacity += props[p]["capacity"]*n
                    durability += props[p]["durability"]*n
                    flavor += props[p]["flavor"]*n
                    texture += props[p]["texture"]*n
                    calories += props[p]["calories"]*n
                if (capacity < 0) or (durability < 0) or (flavor < 0) or (texture < 0):
                    cookie_score.append(0)
                # part 1
                # else: cookie_score.append(capacity*durability*flavor*texture)
                elif calories == 500: cookie_score.append(capacity*durability*flavor*texture)
print(max(cookie_score))