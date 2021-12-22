from pprint import pprint
from functools import reduce
from collections import defaultdict
import hashlib

data = open("input.txt","r").read()

number = 0
hash = hashlib.md5("{}{}".format(data,number).encode()).hexdigest()
# part 1 has with 5 zeros
# part 2 has with 6 zeros
while hash[0:6] != "000000":
    number += 1
    hash = hashlib.md5("{}{}".format(data,number).encode()).hexdigest()
print(number)