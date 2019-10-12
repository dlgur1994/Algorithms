import sys

row,column = map(int,sys.stdin.readline().split())
arr = [[]*column for i in range(row)]
for i in range(row):
    arr[i] = list(list(map(str,sys.stdin.readline()))[:column])

temp = []
temp.append(arr[0][0])
