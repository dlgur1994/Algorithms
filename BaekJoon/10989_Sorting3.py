import sys

num = int(sys.stdin.readline())
numList = []
for _ in range(num):
    numList.append(int(sys.stdin.readline()))

numList.sort()
for e in numList:
    print(e)
