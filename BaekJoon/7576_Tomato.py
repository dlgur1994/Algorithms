import sys

def bfs(x,y):
    visited = [[False for i in range(col)] for j in range(row)]
    queue = []
    queue.append([int(x),int(y)])
    day = 0

    while queue:
        for k in range(len(queue)):
            nodeX,nodeY = queue.pop(0)

            if not visited[nodeX][nodeY]:
                visited[nodeX][nodeY] = True
                if nodeX+1<row and box[nodeX+1][nodeY]=='0':
                    box[nodeX+1][nodeY] = '1'
                    queue.append([nodeX+1,nodeY])
                if nodeX-1>=0 and box[nodeX-1][nodeY]=='0':
                    box[nodeX-1][nodeY] = '1'
                    queue.append([nodeX-1,nodeY])
                if nodeY-1>=0 and box[nodeX][nodeY-1]=='0':
                    box[nodeX][nodeY-1] ='1'
                    queue.append([nodeX,nodeY-1])
                if nodeY+1<col and box[nodeX][nodeY+1]=='0':
                    box[nodeX][nodeY+1] = '1'
                    queue.append([nodeX,nodeY+1])

        if not queue:
            for i in range(row):
                if '0' in box[i]:
                    print("-1")
                    exit(-1)
            print(day)
            print(box)
            break

        day = day+1

col,row = map(int,sys.stdin.readline().split())
box = [[-1 for x in range(col)] for y in range(row)]
for i in range(row):
    box[i] = list(map(str,sys.stdin.readline().split()))

print(box)
bfs(3,5)
