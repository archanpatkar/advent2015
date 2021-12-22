from pprint import pprint
from functools import *
from itertools import *
from collections import *
from random import *
import json

input = { k:int(v) for k,v in [line.split(":") for line in open("input.txt","r").read().split("\n")]}

pprint(input)