import sys

coin,total = map(int,sys.stdin.readline().split())
worth = [0 for i in range(coin+1)]
for i in range(1,coin+1):
    worth[i] = int(sys.stdin.readline())
arr = [sys.maxsize for i in range(total+1)]
arr[0] = 0

for i in range(1,coin+1):
    for j in range(worth[i],total+1):
        if(arr[j]>arr[j-worth[i]]+1):
            arr[j] = arr[j-worth[i]]+1

if(arr[total]==sys.maxsize):
    print(-1)
else:
    print(arr[total])
