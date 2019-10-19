import sys

kind,total = map(int,sys.stdin.readline().split())
worth = [0]*kind
for i in range(0,kind):
    worth[i] = int(sys.stdin.readline())

count = 0
while True:
    if total<0:
        break
    for i in range(kind,0):
        if worth[i]<total:
            total = total-worth[i]
            count = count+1
            break

print(count)
