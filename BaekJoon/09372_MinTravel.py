import sys

testNum = int(sys.stdin.readline())
for i in range(0,testNum):
    node,line = map(int,sys.stdin.readline().split())
    for j in range(0,line):
        dump1,dump2 = map(int,sys.stdin.readline().split())
    print(node-1)
