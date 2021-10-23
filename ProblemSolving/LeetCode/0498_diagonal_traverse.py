import sys
from typing import List

class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        result = []
        row, col = len(mat), len(mat[0])
        x, y = 0, 0
        dir = 'up'
        
        while True:
            result.append(mat[x][y])
            if x==row-1 and y==col-1: break
            if dir == 'up':
                if x > 0 and y < col-1: x, y = x-1, y+1
                else:
                    dir = 'down'
                    if y < col-1: y += 1
                    else: x += 1
            else:
                if x < row-1 and y > 0: x, y = x+1, y-1
                else:
                    dir = 'up'
                    if x < row-1: x += 1
                    else: y += 1

        return result

# Time Limit Exceeded
# class Solution:
#     def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
#         result = [mat[0][0]]
#         dir = 'down'
#         for i in range(1,len(mat)+len(mat[0])-1):
#             for j in range(i+1):
#                 if dir == 'down':
#                     if j<len(mat) and i-j<len(mat[0]):
#                         result.append(mat[j][i-j])
#                 else:
#                     if i-j<len(mat) and j<len(mat[0]):
#                         result.append(mat[i-j][j])
#             dir = 'up' if dir=='down' else 'down'
#         return result

matrix = []
rows = list(sys.stdin.readline().rstrip().lstrip('[').rstrip(']').split('],['))
for row in rows:
    matrix.append(list(map(int, row.split(','))))
mod = Solution()
print(mod.findDiagonalOrder(matrix))