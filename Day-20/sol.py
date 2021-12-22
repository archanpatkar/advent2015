from pprint import pprint
from functools import *
from itertools import *
from collections import *
from random import *
import json
from sympy import divisors
import numpy as np

input = int(open("input.txt","r").read())

print(input)

# Bruteforce algorithm with the bound derived manually (through programmatical experiments)
count = defaultdict(int)
max = 1769229
found = None
for i in range(max):
    print("house:",i)
    # part 1
    # presents = sum([n*10 for n in divisors(i)])
    dvs = divisors(i)
    for d in dvs: count[d] += 1
    presents = sum([n*11 for n in dvs if count[n] <= 50])
    if presents >= input:
        found = i
        break

print(found)