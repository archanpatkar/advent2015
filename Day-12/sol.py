from pprint import pprint
from functools import reduce
from collections import defaultdict
import json

data = json.loads(open("input.txt","r").read())

pprint(data)

# part 1
# def sum(obj):
#     c = 0
#     if isinstance(obj,str): return c
#     if isinstance(obj,dict):
#         for k in obj:
#             if(isinstance(obj[k],int)):
#                 c += obj[k]
#             else: c += sum(obj[k])
#     if isinstance(obj,list):
#         for k in obj:
#             if(isinstance(k,int)):
#                 c += k
#             else: c += sum(k)
#     return c


def sum(obj):
    c = 0
    if isinstance(obj,str): return c
    if isinstance(obj,dict):
        temp = 0
        ignore = False
        for k in obj:
            if(obj[k] == "red"):
                ignore = True
                break
            if(isinstance(obj[k],int)):
                temp += obj[k]
            else: temp += sum(obj[k])
        if not ignore: c += temp
    if isinstance(obj,list):
        for k in obj:
            if(isinstance(k,int)):
                c += k
            else: c += sum(k)
    return c

print(sum(data))