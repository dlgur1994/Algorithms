 import sys
read = sys.stdin.readline().rstrip

voca = read()
count = {}

voca = voca.upper()
for e in voca:
    if e not in count:
        count[e] = 1
    else:
        count[e] += 1


