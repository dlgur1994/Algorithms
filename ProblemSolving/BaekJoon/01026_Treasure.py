numOfNumbers = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
bTemp = b[:]
id = [None] * numOfNumbers
newA = [None] * numOfNumbers

for i in range(0,numOfNumbers):
    id[i] = bTemp.index(max(bTemp))
    bTemp[bTemp.index(max(bTemp))] = -1

for i in range(0,numOfNumbers):
    newA[id[i]] = min(a)
    a[a.index(min(a))] = 101

sum = 0
for i in range(0,numOfNumbers):
    sum += newA[i]*b[i]
print(sum)
