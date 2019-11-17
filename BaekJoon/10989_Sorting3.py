import sys
read = sys.stdin.readline

N = int(read())
numList = [0]*10001
for i in range(N):
    numList[int(read())] += 1

for i in range(10001):
    if numList[i] > 0:
        for j in range(numList[i]):
            print(i)

#'read = sys.stdin.readline' makes the run time short
#'sort' function is slow
