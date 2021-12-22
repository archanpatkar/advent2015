from pprint import pprint
from functools import reduce
from itertools import *
from collections import defaultdict

data = {}
names = set()
for l in open("input.txt","r").readlines():
    l = l.strip().split(" ")
    data[l[0]] = (int(l[3]),int(l[6]),int(l[-2]))
    names.add(l[0])

pprint(data)
pprint(names)
distance = defaultdict(int)
count = defaultdict(int)
points = defaultdict(int)
rest = {}
for i in range(2503):
    for r in names:
        if r in rest and rest[r] == data[r][2]: rest.pop(r)
        if not r in rest:
            distance[r] += data[r][0]
            count[r] += 1
        if count[r] == data[r][1]: 
            rest[r] = 0
            count[r] = 0
        elif r in rest: rest[r] += 1
    m = max([distance[r] for r in distance.keys()])
    for r in names: 
        if distance[r] == m: points[r] += 1
        
pprint(distance)

part1 = [*distance.items()]
part1.sort(key=lambda r: r[1])
print(part1[-1][1])

part2 = [*points.items()]
part2.sort(key=lambda r: r[1])
print(part2[-1][1])