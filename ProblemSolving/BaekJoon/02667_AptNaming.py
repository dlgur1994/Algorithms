import sys

line = int(sys.stdin.readline())
apt = [[-1 for col in range(line)] for row in range(line)]
for i in range(line):
    apt[i] = map(int,sys.stdin.readline().split())

for i in range(line):
    print(list(apt[i]))
