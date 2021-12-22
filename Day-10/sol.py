from pprint import pprint
from functools import reduce
from collections import defaultdict

data = open("input.txt","r").read()

# part 1: 40 times
for i in range(50):
    j = 0
    nd = ""
    while j < len(data):
        count = 0
        curr = data[j]
        j += 1
        count += 1
        while j < len(data) and curr == data[j]:
                j += 1
                count += 1
        nd += "{}{}".format(count,curr)
    data = nd

print(len(data))