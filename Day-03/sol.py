from pprint import pprint
from functools import reduce
from collections import defaultdict

data = open("input.txt","r").read()
visited = defaultdict(int)

# part 1
# x = 0
# y = 0
# for ch in data:
#     visited[(x,y)] += 1
#     if ch == ">": x += 1
#     if ch == "<": x -= 1
#     if ch == "^": y -= 1
#     if ch == "v": y += 1
# print(sum([1 for p in visited if visited[p] >= 1]))

x = [0,0]
y = [0,0]
curr = 0
while curr < len(data):
    # print(ch)
    for i in range(2):
        visited[(x[i],y[i])] += 1
        if data[curr+i] == ">": x[i] += 1
        elif data[curr+i] == "<": x[i] -= 1
        elif data[curr+i] == "^": y[i] -= 1
        elif data[curr+i] == "v": y[i] += 1
    curr += 2
print(sum([1 for p in visited if visited[p] >= 1]))