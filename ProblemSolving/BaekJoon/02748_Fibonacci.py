import sys

def fib(numb):
    arr = [0]*numb
    arr[1] = 1
    for i in range(2,numb):
        arr[i] = arr[i-1]+arr[i-2]
    return arr[numb-1]

num = int(sys.stdin.readline())
result = fib(num+1)
print(result)
