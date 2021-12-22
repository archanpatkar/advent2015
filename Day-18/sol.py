from pprint import pprint
from functools import reduce
from itertools import *
from collections import defaultdict
import json

data = open("input.txt","r").read().split("\n")

grid = defaultdict(int)
for y in range(len(data)):
    for x in range(len(data[y])):
        grid[(x,y)] = 1 if data[y][x] == "#" else 0
# pprint(grid)

neighbours = lambda x,y: [
    (x+1,y+1),(x-1,y-1),
    (x+1,y-1),(x-1,y+1),
    (x,y+1),(x,y-1),
    (x+1,y),(x-1,y)
]

# part 2
always_on = [(0,0),(len(data[0])-1,0),(0,len(data)-1),(len(data[0])-1,len(data)-1)]
for p in always_on: grid[p] = 1
#--

steps = 100
for i in range(steps):
    ng = defaultdict(int)
    for p in grid:
        # part 2
        if p in always_on: ng[p] = 1
        #--
        else:
            count = sum([grid[n] for n in neighbours(*p) if n in grid])
            if grid[p] and count == 2 or count == 3: ng[p] = 1
            elif count == 3: ng[p] = 1
            else: ng[p] = 0
    grid = ng
        
print(sum([grid[p] for p in grid]))