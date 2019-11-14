import sys

def quickSort(arr):
    if len(arr) <= 1:
        return arr
    left, equal, right = [], [], []
    piv = arr[len(arr)//2]
    for e in arr:
        if(e<piv):
            left.append(e)
        elif(e>piv):
            right.append(e)
        else:
            equal.append(e)
    return quickSort(left) + equal + quickSort(right)

num = int(sys.stdin.readline())
numList = list(range(num))
for i in range(num):
    numList[i] = int(sys.stdin.readline())

numList = quickSort(numList)

for e in numList:
    print(e)
