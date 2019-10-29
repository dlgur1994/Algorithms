import sys

def bfs(root):
    visited = [False for i in range(node+1)]
    queue = [root]
    while queue:
        length = len(queue)
        for i in range(length):
            n = queue.pop(0)
            if not visited[n]:
                visited[n] = True
                for j in range(len(graph[n])):
                    queue.append(graph[n][j])
                print(n,end=' ')
    print()

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

for n in graph.keys():
    graph[n] = sorted(graph[n])
bfs(start)
