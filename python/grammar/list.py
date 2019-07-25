num = int(input())
newList = [0] * num
newList = list(map(int,input().split()))

max = newList[num-1]
min = newList[num-1]
for i in range(num-1):
    if(max<newList[i]):
        max = newList[i]
    if(min>newList[i]):
        min = newList[i]

print (min,max)
