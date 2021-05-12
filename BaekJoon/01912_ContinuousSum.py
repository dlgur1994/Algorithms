import sys

num = int(sys.stdin.readline())
arr = list(map(int,sys.stdin.readline().split()))

temp = 0
result = [0 for i in range(num)]
for i in range(0,num):
    temp = temp + arr[i]
    if(temp>0):
        result[i] = temp
    else:
        temp = 0
        result[i] = arr[i]

print(max(result))
