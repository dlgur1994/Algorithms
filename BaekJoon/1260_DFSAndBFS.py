import sys

node,line,start = tuple(map(int,sys.stdin.readline().split()))
graph = dict()
temp1 = list()
temp2 = list()
for i in range(line):
    st,en = tuple(map(int,sys.stdin.readline().split()))
    temp1.append(st)
    temp2.append(en)
    if st not in graph:
        graph[st] = temp2
    elif st in graph:
        graph[st] = graph[st] + temp2
    if en not in graph:
        graph[en] = temp1
    elif en in graph:
        graph[en] = graph[en] + temp1
    temp1 = []
    temp2 = []

print(graph)
