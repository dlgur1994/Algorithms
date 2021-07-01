import sys

read = sys.stdin.readline

def mergeSort(vals):
    l = len(vals)
    # Continue to separate the list until there's only one element.
    if l == 1:
        return vals
    vals1 = vals[:l//2]
    vals2 = vals[l//2:]
    vals1 = mergeSort(vals1)
    vals2 = mergeSort(vals2)

    id1, id2 = 0, 0
    for i in range(l): # Compare the elements of vals1 with the elements of vals2 and make a list in small order
        if id1 == len(vals1):
            vals[i] = vals2[id2]
            id2 += 1
        elif id2 == len(vals2):
            vals[i] = vals1[id1]
            id1 += 1
        elif vals1[id1] > vals2[id2]:
            vals[i] = vals2[id2]
            id2 += 1
        else:
            vals[i] = vals1[id1]
            id1 += 1
    return vals

vals = list(map(int, read().rstrip().split(',')))
print(mergeSort(vals))
