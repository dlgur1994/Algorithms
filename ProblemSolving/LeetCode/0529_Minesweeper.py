from typing import List
from collections import deque
import sys
read = sys.stdin.readline

class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        queue = deque([click])
        directions = [(0,1),(0,-1),(1,0),(-1,0),(-1,-1),(1,-1),(-1,1),(1,1)]
        while queue:
            row,col = queue.popleft()
            if board[row][col]=='M':
                board[row][col]='X'
                return board
            if board[row][col]=='B':
                continue

            check = ['M','E']
            options = 'B12345678'
            cnt = 0
            temp = []
            for rd,cd in directions:
                nrow,ncol = row+rd,col+cd
                if -1<nrow<len(board) and -1<ncol<len(board[0]) and board[nrow][ncol] in check:
                    if board[nrow][ncol]=='M':
                        cnt += 1
                    else:
                        temp.append((nrow,ncol))
            if cnt==0:
                queue.extend(temp)
            board[row][col]=options[cnt]
        return board

input = list(read().rstrip().lstrip('[').rstrip(']').split('],['))
click = list(map(int,read().rstrip().lstrip('[').rstrip(']').split(',')))
input_refined = []
for e in input:
    input_refined.append(list(e.split(',')))
mod = Solution()
print(mod.updateBoard(input_refined,click))
# [[E,E,E,E,E],[E,E,M,E,E],[E,E,E,E,E],[E,E,E,E,E]]
