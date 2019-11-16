import sys

num = int(sys.stdin.readline())
peoDict = dict()
for _ in range(num):
    age,name = sys.stdin.readline().split()
    peoDict[name] = age

for name,age in sorted(peoDict.items(), key=lambda x: x[1]):
    print (age,name)
