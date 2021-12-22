from pprint import pprint
from functools import reduce
from collections import defaultdict

data = []
for l in open("input.txt","r").readlines():
    l = l.strip().split("=")
    l[0] = l[0].strip().split(" ")
    l[0] = [l[0][0],l[0][2]]
    l[1] = int(l[1])
    data.append(l)
pprint(data)

graph = {}
for route in data:
    if not route[0][0] in graph: graph[route[0][0]] = []
    if not route[0][1] in graph: graph[route[0][1]] = []
    graph[route[0][0]].append((route[0][1],route[1]))
    graph[route[0][1]].append((route[0][0],route[1]))

pprint(graph)

rlen = []
def route(node,cost,visited=[]):
    visited.append(node)
    for r in graph[node]: 
        if not (r[0] in visited):
            route(r[0],cost+r[1],[*visited])
    if len(visited) == len(graph.keys()): rlen.append(cost)

for n1 in graph: route(n1,0,[])

print(min(rlen))
print(max(rlen))