from pprint import pprint
from functools import reduce
from collections import defaultdict

data = [l.strip() for l in open("input.txt","r").readlines()]
pprint(data)

# part 1
# vowels = ["a","e","i","o","u"]
# forbidden = ["ab", "cd", "pq", "xy"]
# nice = 0
# for line in data:
#     vows = sum([1 for ch in line if ch in vowels])
#     double = sum([1 for i in range(len(line)-1) if line[i] == line[i+1]])
#     wrong = sum([1 for i in range(len(line)-1) if "{}{}".format(line[i],line[i+1]) in forbidden])
#     if vows >= 3 and double > 0 and wrong == 0: 
#         nice += 1
# print(nice)

nice = 0
for line in data:
    pairs = defaultdict(lambda: set())
    for i in range(0,len(line)-1,1): pairs["{}{}".format(line[i],line[i+1])].update((i,i+1))
    right = sum([1 for p in pairs if (len(pairs[p])/2) >= 2])
    gapped = sum([1 for i in range(len(line)-2) if line[i] == line[i+2]])
    if right >= 1 and gapped >= 1: 
        nice += 1
print(nice)