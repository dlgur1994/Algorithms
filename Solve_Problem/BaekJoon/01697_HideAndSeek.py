import sys

def bfs(root):
    visited = [False]*100001
    queue = [root]
    time = 0
    find = False

    while queue:
        for i in range(len(queue)):
            node = queue.pop(0)
            if not visited[node]:
                visited[node]=True
                if node==bro:
                    find = True
                    break
                if node+1<=100000:
                    queue.append(node+1)
                if node-1>=0:
                    queue.append(node-1)
                if node*2<=100000:
                    queue.append(node*2)

        if find==True:
            print(time)
            break

        time = time+1

subin,bro = map(int,sys.stdin.readline().split(" "))
bfs(subin)
