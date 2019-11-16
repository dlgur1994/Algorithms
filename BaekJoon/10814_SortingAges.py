import sys

num = int(sys.stdin.readline())
peoDict = dict()
for _ in range(num):
    age,name = sys.stdin.readline().split()
    peoDict[name] = age

valueList = sorted(peoDict.values())
nameList = list()
for i in range(num):
    for name,age in peoDict.items():
        if age == valueList[i]:
            nameList.append(name)
            peoDict[name] = -1

for i in range(num):
    print(valueList[i],nameList[i])
