import sys

coin,total = map(int,sys.stdin.readline().split())
worth = [0]*(coin+1)
for i in range(1,coin+1):
    worth[i] = int(sys.stdin.readline())
arr = [[sys.maxsize for col in range(total+1)] for row in range(coin+1)]
arr[0][0] = 0
for i in range(1,total+1):
    arr[0][i]=sys.maxsize
for i in range(1,coin+1):
    arr[i][0] = 0

for i in range(1,coin+1):
    for j in range(1,total+1):
        if(worth[i]>j):
            arr[i][j] = arr[i-1][j]
        elif(arr[i-1][j]>arr[i][j-worth[i]]+1):
            arr[i][j] = arr[i][j-worth[i]]+1
        else:
            arr[i][j] = arr[i-1][j]

if(arr[coin][total]==sys.maxsize):
    print(-1)
else:
    print(arr[coin][total])
