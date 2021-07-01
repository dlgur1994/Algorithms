import sys

def quickSort(arr):
    largList, smalList, sameList = [], [], []

    if len(arr) <= 1:
        return arr
    piv = arr[0]
    for i in range(len(arr)):
        if(arr[i]<piv):
            smalList.append(arr[i])
        elif(arr[i]>piv):
            largList.append(arr[i])
        else:
            sameList.append(arr[i])

    return quickSort(smalList) + sameList + quickSort(largList)

num = int(sys.stdin.readline())
numList = list(range(num))
for i in range(num):
    numList[i] = int(sys.stdin.readline())

numList = quickSort(numList)
for i in range(num):
    print(numList[i])
