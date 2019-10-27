import sys

def bfs(x,y):
    visited = [[False for i in range(col)] for j in range(row)]
    queue = []
    queue.append([x,y])
    day = 0

    while queue:
        for k in range(len(queue)):
            nodeX,nodeY = queue.pop(0)

            if not visited[nodeX][nodeY]:
                visited[nodeX][nodeY] = True
                if nodeX+1<row and box[nodeX+1][nodeY]==0:
                    box[nodeX+1][nodeY] = 1
                    queue.append([nodeX+1,nodeY])
                if nodeX-1>=0 and box[nodeX-1][nodeY]==0:
                    box[nodeX-1][nodeY] = 1
                    queue.append([nodeX-1,nodeY])
                if nodeY-1>=0 and box[nodeX][nodeY-1]==0:
                    box[nodeX][nodeY-1] =1
                    queue.append([nodeX,nodeY-1])
                if nodeY+1<col and box[nodeX][nodeY+1]==0:
                    box[nodeX][nodeY+1] = 1
                    queue.append([nodeX,nodeY+1])

        if not queue:
            print(day)
            print(box)
            break

        day = day+1

'''
        if queue.empty():
            print("-1")
            break
'''

col,row = map(int,sys.stdin.readline().split())
box = [[-1 for x in range(col)] for y in range(row)]
for i in range(row):
    box[i] = list(map(int,sys.stdin.readline().split()))

print(box)
bfs(3,5)
