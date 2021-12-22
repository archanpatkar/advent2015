from pprint import pprint
from functools import reduce
from collections import defaultdict

data = [l.strip()[1:-1] for l in open("input.txt","r").readlines()]
# pprint(data)

total1 = sum([len(str)+2 for str in data])
print("total1:",total1)

total2 = 0
total3 = 0
# subs = []
for st in data:
    count = 0
    count2 = 6
    i = 0
    while i < len(st):
        if st[i] == "\\":
            if st[i+1] == "\\":
                i += 2
                count += 1
                count2 += 4
            elif st[i+1] == "\"":
                i += 2
                count += 1
                count2 += 4
            elif st[i+1] == "x":
                i += 4
                count += 1
                count2 += 5
        else: 
            i += 1    
            count += 1
            count2 += 1
    print("subcount:",count)
    print("subcount2:",count2)
    total2 += count
    total3 += count2

print("total2:",total2)
print(total1-total2)
print("total3:",total3)
print(total3-total1)