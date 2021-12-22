from pprint import pprint
from functools import reduce

rects = [tuple(map(int,l.strip().split("x"))) for l in open("input.txt","r").read().split("\n")]
pprint(rects)

print(sum([2*r[0]*r[1] + 2*r[1]*r[2] + 2*r[2]*r[0] + min([r[0]*r[1],r[1]*r[2],r[2]*r[0]]) for r in rects]))

print(sum([2*r[0] + 2*r[1] + reduce(lambda x,y:x*y, r) for r in map(sorted,rects)]))