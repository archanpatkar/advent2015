from pprint import pprint
from functools import reduce
from itertools import *
from collections import defaultdict
# from queue import PriorityQueue
# from difflib import SequenceMatcher
from random import choice


data = open("input.txt","r").read().split("\n")

molecule = data[-1]
transforms = defaultdict(lambda: [])
reverse = {}
for p,e in [s.strip().split("=>") for s in data[:-2]]:
    transforms[p.strip()].append(e.strip())
    reverse[e.strip()] = p.strip()

pprint(transforms)
print(molecule)

cache = {}
def replace(molecules):
    if isinstance(molecules, str):
        if molecules in cache: return cache[molecules]
        else: cache[molecules] = replace([molecules])
        return cache[molecules]
    distinct = set()
    if isinstance(molecules,list):
        for molecule in molecules:
            if molecule in cache: distinct.update(cache[molecule])
            else:
                permol = set()
                molecule_str = molecule
                molecule = list(molecule)
                for i in range(len(molecule)):
                    if molecule[i] in transforms:
                        for ch in transforms[molecule[i]]:
                            nm = [*molecule]
                            nm[i] = ch
                            permol.add("".join(nm))
                    if i+1 < len(molecule) and (molecule[i] + molecule[i+1] in transforms):   
                        for ch in transforms[molecule[i]+molecule[i+1]]:
                            nm = [*molecule]
                            nm.pop(i)
                            nm.pop(i)
                            nm.insert(i,ch)
                            permol.add("".join(nm))
                cache[molecule_str] = permol
                distinct.update(permol)
    return distinct

# part 1
print(len(replace(molecule)))

# part2
# Read some reddit hints as well as some solutions which recommended 
# using randomness for substituting in reverse order to the root node
curr = molecule
steps = 0
while curr != "e":
    rep,sub = choice(list(reverse.items()))
    if rep in curr:
        curr = curr.replace(rep,sub,1)
        steps += 1
print(steps)



# A* algo for finding the molecule but takes too long to compute!
# def closeness(str,str2):
#     if len(str) > len(str2): return None
#     flag = True
#     continous = 0
#     nm = 0
#     for i in range(len(str)):
#         if str[i] == str2[i] and flag: 
#             continous += 1
#         else:
#             nm += 1
#             flag = False
#     return nm-continous

# def similar(a, b):
#     return SequenceMatcher(None, a, b).ratio()

# start = "e"
# end = molecule
# current_nodes = set(["e"])
# queue = PriorityQueue()
# queue.put((0,start))
# distance = defaultdict(lambda: -1)
# distance[start] = 0
# step = 0
# len_end = len(end)

# while not queue.empty():
#     print("step:",step)
#     priority,current = queue.get()
#     # current_nodes.remove(current)
#     if current == end: break
#     for next in replace(current):
#         # print("next:",next)
#         # print("closeness:",closeness(next,end))
#         if len(next) > len_end: continue
#         print("diff:",len(molecule)-len(next))
#         cost = distance[current] + 1
#         if (not next in distance) or cost < distance[next]:
#             distance[next] = cost
#             # cost +
#             priority = similar(next,end) * 10
#             print("priority:",-priority)
#             # visited.add(next)
#             # if:
#             #  (next not in current_nodes) and
#             # if  priority != None:
#                 # (cost + (-priority)
#             queue.put((-priority,next))
#             # current_nodes.add(next)
#         if end in distance: break
#     step += 1
# print(distance[end])