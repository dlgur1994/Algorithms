import sys
from itertools import combinations

vowels = ['a','e','i','o','u']
length,type = map(int,sys.stdin.readline().split())
typeList = map(str,sys.stdin.readline().split())

madeList = list(map(''.join, combinations(sorted(typeList),length)))
for e in madeList:
    vCount = 0
    for c in e:
        if c in vowels:
            vCount = vCount + 1
    if vCount>0 and vCount<length-1:
        print(e)
