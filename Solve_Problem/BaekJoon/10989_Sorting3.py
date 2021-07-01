import sys
read = sys.stdin.readline

N = int(read())
numList = [0]*10001
for i in range(N):
    numList[int(sys.stdin.readline())] += 1

for i in range(10001):
    if numList[i] > 0:
        print('{}\n'.format(i) * numList[i], end='')

#'read = sys.stdin.readline' makes the run time short
#'sort' function is slow
#'{}'.format(value) --> {} is substituted by 'value'
