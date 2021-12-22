from pprint import pprint
from functools import reduce
from itertools import *
from collections import defaultdict
import json

data = [int(l) for l in open("input.txt","r").readlines()]

pprint(data)

combs = defaultdict(int)
for i in range(1,len(data)):
    for c in combinations(data,i):
        if sum(c) == 150: combs[c] += 1

pprint(combs)
# part 1
print(sum([combs[k] for k in combs]))

# part 2
clen = min([len(c) for c in combs])
print(sum([combs[k] for k in combs if len(k) == clen]))