import sys
read = sys.stdin.readline

class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        def bfs(row,col):
            visited = []
            queue = deque([(row,col)])
            while queue:
                r,c = queue.popleft()
                if node not in visited:
                    visited.append(node)
                queue.append(node)

        while True:
            row,col = read().rstrip.lstrip('[').rstrip(']').split(',')


input = list(read().rstrip().lstrip('[').rstrip(']').split('],['))
input_refined = []
for e in input:
    input_refined.append(list(e.split(',')))
mod = Solution()
print(mod.updateBoard(input_refined))
# [[E,E,E,E,E],[E,E,M,E,E],[E,E,E,E,E],[E,E,E,E,E]]


# from typing import List
# from collections import deque
# import sys
# read = sys.stdin.readline

# class Solution:
#     def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
#         def checkAround(r,c):
#             if r>0 and board[r-1][c]=='M':
#                 return
#             if r<len(board)-1 and board[r+1][c]=='M':
#                 return
#             if c>0 and board[r][c-1]=='M':
#                 return
#             if c<len(board[0])-1 and board[r][c+1]=='M':
#                 return
#             if r>0 and c>0 and board[r-1][c-1]=='M':
#                 return
#             if r>0 and c<len(board[0])-1 and board[r-1][c+1]=='M':
#                 return
#             if r<len(board)-1 and c>0 and board[r+1][c-1]=='M':
#                 return
#             if r<len(board)-1 and c<len(board[0])-1 and board[r+1][c+1]=='M':
#                 return
#             board[r][c]='B'

#         def bfs(r,c):
#             r = int(r)
#             c = int(c)
#             visited = []
#             queue = deque([(r,c)])
#             while queue:
#                 row,col = queue.popleft()
#                 if (row,col) not in visited:
#                     visited.append((row,col))
#                     checkAround(row,col)
#                     if row>0 and (row-1,col) not in visited:
#                         queue.append((row-1,col))
#                     if row<len(board)-1 and (row+1,col) not in visited:
#                         queue.append((row+1,col))
#                     if col>0 and (row,col-1) not in visited:
#                         queue.append((row,col-1))
#                     if col<len(board[0])-1 and (row,col+1) not in visited:
#                         queue.append((row,col+1))
#             print(board)

#         for i in range(len(board)):
#             for j in range(len(board[0])):
#                 if board[i][j]=='M':
#                     if click[0]==str(i) and click[1]==str(j):
#                         board[i][j]='X'
#                         return board
#         bfs(click[0],click[1])
