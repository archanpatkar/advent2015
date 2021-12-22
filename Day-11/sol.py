from pprint import pprint
from functools import reduce
from collections import defaultdict

data = open("input.txt","r").read()

start = ord("a")

chars = [ord(ch)-start for ch in data]
print(chars)

convert = lambda a: "".join([chr(start+e) for e in a])
print(convert(chars))

def isvalid(str):
    print(str)
    if "i" in str or "o" in str or "l" in str: return False
    count1 = 0
    for i in range(len(str)-3):
        fst = ord(str[i])
        if fst+1 == ord(str[i+1]) and fst+2 == ord(str[i+2]): 
            count1 += 1
            break
    index = set()
    for i in range(0,len(str)-1):
        if str[i] == str[i+1]: 
            index.add(i)
            index.add(i+1)
    return True if count1 > 0 and len(index)/2 >= 2 else False

def update(inc,chars):
    chars[inc] = (chars[inc] + 1) % 26
    if chars[inc] in [9,12,15]: chars[inc] += 1
    if(chars[inc] == 0): update(inc-1,chars)

inc = len(chars)-1
passwords = []
for i in range(2):
    while not isvalid(convert(chars)):
        update(inc,chars)
    passwords.append(convert(chars))
    update(inc,chars)
print(passwords)