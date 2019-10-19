import sys

def fiv(numb):
    arr = [0]*numb
    if(numb==1):
        return 0
    elif(numb==2):
        return 1
    else:
        arr[1] = 1
        for i in range(2,numb):
            arr[i] = arr[i-1]+arr[i-2]
        return arr[numb-1]

num = int(sys.stdin.readline())
result = fiv(num+1)
print(result)
