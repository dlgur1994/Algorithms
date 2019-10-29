import sys

node,line,start = tuple(map(int,sys.stdin.readline().split()))
graph = dict()
temp = list()
for i in range(line):
    st,en = tuple(map(int,sys.stdin.readline().split()))
    temp.append(en)
    if st not in graph:
        graph[st] = temp
    else:
        graph[st] = graph[st] + temp
    temp = []
