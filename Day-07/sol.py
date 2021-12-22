from pprint import pprint
from functools import reduce
from collections import defaultdict
import ctypes


data = []
for l in open("input.txt","r").readlines():
    l = l.strip().split("->")
    # print(l)
    if l[0].isnumeric(): 
        l[0] = int(l[0])
    else:
        op = list(filter(lambda s: len(s) > 0,l[0].split(" ")))
        for i in range(len(op)):
            if(op[i].isnumeric()):
                op[i] = int(op[i])
            else: op[i] = op[i].strip()
        l[0] = op[0] if len(op) == 1 else op
    l[1] = l[1].strip()
    data.append(l)
# pprint(data)


ops = {
    "AND": lambda x,y: x & y,
    "OR": lambda x,y: x | y,
    "LSHIFT": lambda x,y: x << y,
    "RSHIFT": lambda x,y: x >> y,
    "NOT": lambda x: ~x
}

circuit = {}
has = defaultdict(lambda: [])
pending = []

for op in data: 
    circuit[op[1]] = op[0]
    if isinstance(op[0],list):
        for o in op[0]:
            print(o)
            if not o in ops and not isinstance(o,int):
                has[o].append(op[1])

val = []
done = 0
while done < len(circuit.keys()):
    # pprint(circuit)
    # pprint(has)
    print("done:",done)
    print("keys:",len(circuit.keys()))
    done = 0
    for k in circuit:
        if isinstance(circuit[k],int): 
            done += 1
            for op in has[k]:
                if not op in val:
                    if isinstance(circuit[op],str):
                        circuit[op] = circuit[k]
                    else:
                        print(circuit[op])
                        n = 0
                        for i in range(len(circuit[op])):
                            if isinstance(circuit[op][i],int): n += 1
                            if circuit[op][i] == k: 
                                circuit[op][i] = circuit[k]
                                n += 1
                        print("n: ",n)
                        if len(circuit[op]) == 2 and n == 1:
                            circuit[op] = ctypes.c_ushort(ops[circuit[op][0]](circuit[op][1])).value 
                            val.append(op)
                            done += 1
                        elif len(circuit[op]) == 3 and n == 2:
                            circuit[op] = ctypes.c_ushort(ops[circuit[op][1]](circuit[op][0],circuit[op][2])).value 
                            val.append(op)
                            done += 1
print("done:",done)
pprint(circuit)