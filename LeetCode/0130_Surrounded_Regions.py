from typing import List
import sys
read = sys.stdin.readline

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        def getLink():
            for i in range(len(board)-1):
                for j in range(len(board[0])-1):
                    temp = []
                    if board[i][j]=='o':
                        if board[i+1][j]== 'o':
                            temp.append((i+1)*len(board)+j)
                        if board[i][j+1]== 'o':
                            temp.append(i*len(board)+j+1)
                    link.append(temp)
                link.append([])

        def dfs(start):
            visited = []
            stack = [start,[start]]
            while stack:
                node,next = stack.pop()
                if node not in visited:
                    visited.append(node)
                if link[next]==[]:
                    routes.append(visited)
        link = []
        routes = []
        getLink()
        dfs(5)

input = list(read().rstrip().lstrip('[[').rstrip(']]').split('],['))
for i in range(len(input)):
    input[i] = input[i].split(',')
mod = Solution()
mod.solve(input)
#print(input)
