import sys

def dfs(root):
    visited = [False for i in range(node+1)]
    stack = [root]
    temp = []
    result = []
    while stack:
        n = stack.pop(0)
        if not visited[n]:
            visited[n] = True
            for child in graph[n]:
                if not visited[child]:
                    temp.append(child)
            stack = temp + stack
            temp = []
            result.append(n)
    return result

node = int(sys.stdin.readline())
line = int(sys.stdin.readline())
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

result = dfs(1)
print(len(result)-1)
