import sys

num = int(sys.stdin.readline())
numList = list(range(num))
for i in range(num):
    numList[i] = int(sys.stdin.readline())

numList = sorted(numList)

for e in numList:
    print(e)
